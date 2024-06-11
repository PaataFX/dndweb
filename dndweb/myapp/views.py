from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.db.models import Q
from django.core.files.storage import default_storage
from django.conf import settings
from .models import (
    Rarity, Armor, Property, Weapon, Tool, AbilityScore, Skill, SavingThrow, 
    Class, Subclass, Race, Subrace, Spell, Language, Feat, Character, 
    Proficiency, Equipment, Trait
)
from .forms import MyUserCreationForm, CustomUserUpdateForm, CustomCharacterForm
from django.shortcuts import redirect



User = get_user_model()

# Utility functions
def calculate_modifier(score):
    return (score - 10) // 2

# Main views
def index(request):
    races = Race.objects.all()
    classes = Class.objects.all()
    spells = Spell.objects.all()
    return render(request, 'index.html', {'races': races, 'classes': classes, 'spells': spells})

def armor_list(request):
    light_armors = Armor.objects.filter(weight_class='Light')
    medium_armors = Armor.objects.filter(weight_class='Medium')
    heavy_armors = Armor.objects.filter(weight_class='Heavy')
    no_weight_class_armors = Armor.objects.filter(weight_class='None')
    
    return render(request, 'armor_list.html', {
        'light_armors': light_armors,
        'medium_armors': medium_armors,
        'heavy_armors': heavy_armors,
        'no_weight_class_armors': no_weight_class_armors,
    })

# Authentication views
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username:
            username = username.lower()
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Username is required.')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please check the form and try again.')
            for field in form.errors:
                messages.error(request, f"{field.capitalize()} error: " + ', '.join(form.errors[field]))

    context = {'form': form}
    return render(request, 'base/login_register.html', context)

@login_required
def userProfile(request):
    return render(request, 'user_profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST['username']
        email = request.POST['email']
        avatar = request.FILES.get('avatar')

        user.username = username
        user.email = email

        if avatar:
            if user.avatar:
                old_file_path = user.avatar.path
                if old_file_path != str(settings.MEDIA_ROOT / 'avatars/default_avatar.jpeg'):
                    default_storage.delete(old_file_path)
            user.avatar = avatar

        user.save()
        messages.success(request, 'Your profile was successfully updated!')
        return redirect('profile_update')
    else:
        return render(request, 'user_profile.html')

# Character views
@login_required
def character_list(request):
    characters = Character.objects.filter(player=request.user)
    return render(request, 'character_list.html', {'characters': characters})

def character_detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'character_detail.html', {'character': character})

def character_detail(request, character_id):
    character = get_object_or_404(Character, id=character_id)

    if request.method == 'POST':
        # Update character attributes based on submitted form data
        character.name = request.POST.get('charname', character.name)
        class_level = request.POST.get('classlevel', f"{character.dnd_class.name} {character.level}").split()
        if len(class_level) > 1:
            character.dnd_class.name = class_level[0]
            character.level = class_level[1]
        character.subclass = request.POST.get('subclass', character.subclass)
        character.player = request.POST.get('playername', character.player)
        race_subrace = request.POST.get('race', f"{character.race} - {character.subrace}").split('-')
        if len(race_subrace) > 1:
            character.race = race_subrace[0].strip()
            character.subrace = race_subrace[1].strip()
        character.alignment = request.POST.get('alignment', character.alignment)
        character.experience_points = request.POST.get('experiencepoints', character.experience_points)
        
        character.strength = request.POST.get('Strengthscore', character.strength)
        character.dexterity = request.POST.get('Dexterityscore', character.dexterity)
        character.constitution = request.POST.get('Constitutionscore', character.constitution)
        character.wisdom = request.POST.get('Wisdomscore', character.wisdom)
        character.intelligence = request.POST.get('Intelligencescore', character.intelligence)
        character.charisma = request.POST.get('Charismascore', character.charisma)

        character.inspiration = 'inspiration' in request.POST
        character.proficiency_bonus = request.POST.get('proficiencybonus', character.proficiency_bonus)
        
        character.passive_perception = request.POST.get('passiveperception', character.passive_perception)
        character.other_proficiencies = request.POST.get('otherprofs', character.other_proficiencies)

        character.armor_class = request.POST.get('ac', character.armor_class)
        character.initiative = request.POST.get('initiative', character.initiative)
        character.speed = request.POST.get('speed', character.speed)
        character.max_hit_points = request.POST.get('maxhp', character.max_hit_points)
        character.hit_points = request.POST.get('currenthp', character.hit_points)
        character.temporary_hit_points = request.POST.get('temphp', character.temporary_hit_points)
        character.hit_dice_total = request.POST.get('totalhd', character.hit_dice_total)
        character.hit_dice_remaining = request.POST.get('remaininghd', character.hit_dice_remaining)
        character.death_saves_successes = sum(1 for i in range(1, 4) if f'deathsuccess{i}' in request.POST)
        character.death_saves_failures = sum(1 for i in range(1, 4) if f'deathfail{i}' in request.POST)

        character.cp = request.POST.get('cp', character.cp)
        character.sp = request.POST.get('sp', character.sp)
        character.ep = request.POST.get('ep', character.ep)
        character.gp = request.POST.get('gp', character.gp)
        character.pp = request.POST.get('pp', character.pp)

        character.personality = request.POST.get('personality', character.personality)
        character.ideals = request.POST.get('ideals', character.ideals)
        character.bonds = request.POST.get('bonds', character.bonds)
        character.flaws = request.POST.get('flaws', character.flaws)
        character.features = request.POST.get('features', character.features)

        character.equipment_list = request.POST.get('equipment_list', character.equipment_list)
        character.attacks_description = request.POST.get('attacks_description', character.attacks_description)
        
        # Update attacks and spellcasting
        for i, attack in enumerate(character.attacks.all()):
            attack.name = request.POST.get(f'atkname{i + 1}', attack.name)
            attack.attack_bonus = request.POST.get(f'atkbonus{i + 1}', attack.attack_bonus)
            attack.damage_type = request.POST.get(f'atkdamage{i + 1}', attack.damage_type)
            attack.save()
        
        character.save()
        
        return redirect('character_sheet', character_id=character.id)
    
    context = {
        'character': character,
        'proficiency_bonus': character.proficiency_bonus,
        'saving_throws': character.get_saving_throws(),  # Assuming you have this method in your model
        'skills': character.get_skills()  # Assuming you have this method in your model
    }
    return render(request, 'character_detail.html', context)

@login_required
def delete_character(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    if request.method == 'POST':
        character.delete()
        return redirect('character_list')
    return render(request, 'character_detail.html', {'character': character})

def create_character(request):
    if request.method == 'POST':
        form = CustomCharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.player = request.user
            if not character.hit_points:
                character.hit_points = 10
            if not character.max_hit_points:
                character.max_hit_points = 10
            if not character.temporary_hit_points:
                character.temporary_hit_points = 0
            if not character.armor_class:
                character.armor_class = 10
            if not character.initiative:
                character.initiative = 0
            if not character.speed:
                character.speed = 30
            if not character.experience_points:
                character.experience_points = 0
            if not character.proficiency_bonus:
                character.proficiency_bonus = 2
            character.save()
            form.save_m2m()  # Save many-to-many fields
            return redirect('character_detail', character_id=character.id)
    else:
        form = CustomCharacterForm()

    context = {
        'form': form,
        'races': Race.objects.all(),
        'subraces': Subrace.objects.all(),
        'classes': Class.objects.all(),
        'subclasses': Subclass.objects.all(),
        'saving_throws': SavingThrow.objects.all(),
        'skills': Skill.objects.all(),
        'languages': Language.objects.all(),
        'proficiencies': Proficiency.objects.all(),
        'equipment': Equipment.objects.all(),
        'spells': Spell.objects.all(),
        'features': Trait.objects.all(),
    }
    return render(request, 'create_character.html', context)

# Race views
def races_page(request):
    races = Race.objects.all()
    return render(request, 'races_page.html', {'races': races})

def race_detail(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    return render(request, 'race_detail.html', {'race': race})

# Class views
def classes_page(request):
    classes = Class.objects.all()
    return render(request, 'classes_page.html', {'classes': classes})

def class_detail(request, class_id):
    class_obj = get_object_or_404(Class, pk=class_id)
    return render(request, 'class_detail.html', {'class_obj': class_obj})

# Spell views
def spells_page(request):
    spells = Spell.objects.all()
    levels = set(spell.level for spell in spells)
    return render(request, 'spells_page.html', {'spells': spells, 'levels': sorted(levels)})

# Character detail with additional calculations
def character_detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    skills = Skill.objects.all()
    saving_throws = SavingThrow.objects.all()
    proficiency_bonus = character.proficiency_bonus
    ability_modifiers = {
        'Strength': calculate_modifier(character.strength),
        'Dexterity': calculate_modifier(character.dexterity),
        'Constitution': calculate_modifier(character.constitution),
        'Wisdom': calculate_modifier(character.wisdom),
        'Intelligence': calculate_modifier(character.intelligence),
        'Charisma': calculate_modifier(character.charisma),
    }

    return render(request, 'character_detail.html', {
        'character': character,
        'skills': skills,
        'proficiency_bonus': proficiency_bonus,
        'ability_modifiers': ability_modifiers,
    })


@login_required
def character_list(request):
    characters = Character.objects.all()
    return render(request, 'character_list.html', {'characters': characters})

@login_required
def delete_character(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    if request.method == 'POST':
        character.delete()
        return redirect('characters')  # Update the URL name here
    return render(request, 'character_detail.html', {'character': character})

from .models import Spell

def spell_list(request):
    spells = Spell.objects.all()
    levels = [spell.level for spell in spells]
    levels = list(set(levels))  # Get unique levels
    levels.sort()
    context = {
        'spells': spells,
        'levels': levels
    }
    return render(request, 'spell_list.html', context)

def spell_detail(request, spell_id):
    spell = get_object_or_404(Spell, pk=spell_id)
    context = {
        'spell': spell
    }
    return render(request, 'spell_detail.html', context)
