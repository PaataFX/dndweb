from django.shortcuts import render
from .models import Rarity, Armor, Property, Weapon, Tool, AbilityScore, Skill, SavingThrow, Class, Subclass, Race, Subrace, Spell, Language, Feat

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, "home.html")

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

def characters(request):
    return render(request, 'character_html.html')

def login(request):
    return render(request, 'login.html')
