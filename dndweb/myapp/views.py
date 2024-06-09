from django.shortcuts import render
from .models import Rarity, Armor, User, Property, Weapon, Tool, AbilityScore, Skill, SavingThrow, Class, Subclass, Race, Subrace, Spell, Language, Feat
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm
from .forms import CustomUserUpdateForm
from.models import Character
from django.shortcuts import get_object_or_404

from .models import Race, Class, Spell

def index(request):
    races = Race.objects.all()
    classes = Class.objects.all()
    spells = Spell.objects.all()
    return render(request, 'index.html', {'races': races, 'classes': classes, 'spells': spells})


def home(request):
    races = Race.objects.all()
    classes = Class.objects.all()
    spells = Spell.objects.all()
    return render(request, 'home.html', {'races': races, 'classes': classes, 'spells': spells})

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



from django.contrib.auth import get_user_model
User = get_user_model()



def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username:
            username = username.lower()  # Normalize the username to lowercase
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'სახელი ან პაროლი არ არსებობს')
        else:
            messages.error(request, 'საჭიროა სახელი.')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()  # Normalize the username to lowercase
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

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import default_storage
from django.conf import settings

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







from django.shortcuts import render, redirect
from .models import Character

def character_list(request):
    if request.user.is_authenticated:
        characters = Character.objects.filter(player=request.user)  # Use 'player' instead of 'user'
        context = {'characters': characters}
        return render(request, 'character_list.html', context)
    else:
        return redirect('login')


from django.shortcuts import render, get_object_or_404
from .models import Character

def character_detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'character_detail.html', {'character': character})


from django.shortcuts import render, redirect
from .forms import CustomCharacterForm
from .models import Race, Subrace, Class, Subclass, SavingThrow, Skill, Language, Proficiency, Equipment, Spell, Trait

def create_character(request):
    if request.method == 'POST':
        form = CustomCharacterForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.player = request.user
            # Ensure default values for optional fields if not provided
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
        'skills': Skill.objects.all(),  # Fixed typo
        'languages': Language.objects.all(),
        'proficiencies': Proficiency.objects.all(),
        'equipment': Equipment.objects.all(),
        'spells': Spell.objects.all(),
        'features': Trait.objects.all(),
    }
    return render(request, 'create_character.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Character  # Assuming you have a Character model

def character_detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    return render(request, 'character_detail.html', {'character': character})


from django.shortcuts import render
from .models import Character


from .models import Race

def races_page(request):
    races = Race.objects.all()  # Assuming Race is the name of your model for races
    return render(request, 'races_page.html', {'races': races})


def race_detail(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    return render(request, 'race_detail.html', {'race': race})

from .models import Class

def classes_page(request):
    classes = Class.objects.all()
    return render(request, 'classes_page.html', {'classes': classes})


from .models import Class

def class_detail(request, class_id):
    class_obj = get_object_or_404(Class, pk=class_id)
    return render(request, 'class_detail.html', {'class_obj': class_obj})

from .models import Spell

def spells_page(request):
    spells = Spell.objects.all()
    # Get unique spell levels
    levels = set(spell.level for spell in spells)
    return render(request, 'spells_page.html', {'spells': spells, 'levels': sorted(levels)})


# views.py
from django.shortcuts import render
from .models import Skill, Character

def calculate_modifier(score):
    return (score - 10) // 2

def character_detail(request, character_id):
    character = Character.objects.get(pk=character_id)
    skills = Skill.objects.all()
    proficiency_bonus = character.proficiency_bonus
    ability_modifiers = {
        'Strength': calculate_modifier(character.strength),
        'Dexterity': calculate_modifier(character.dexterity),
        'Constitution': calculate_modifier(character.constitution),
        'Wisdom': calculate_modifier(character.wisdom),
        'Intelligence': calculate_modifier(character.intelligence),
        'Charisma': calculate_modifier(character.charisma),
    }
    
    # Add calculated ability modifiers to the ability_modifiers dictionary
    for ability, score in ability_modifiers.items():
        ability_modifiers[ability] = calculate_modifier(score)

    return render(request, 'character_detail.html', {
        'character': character,
        'skills': skills,
        'proficiency_bonus': proficiency_bonus,
        'ability_modifiers': ability_modifiers,
    })

