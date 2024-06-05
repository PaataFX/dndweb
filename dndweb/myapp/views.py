from django.shortcuts import render
from .models import Rarity, Armor, User, Property, Weapon, Tool, AbilityScore, Skill, SavingThrow, Class, Subclass, Race, Subrace, Spell, Language, Feat
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm

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
    return render(request, 'charactersheet.html')



def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'მომხმარებელი არ არსებობს')
            return render(request, 'base/login_register.html', {'page': page})

        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'სახელი ან პაროლი არ არსებობს')

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
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            # Form validation failed, provide specific error messages
            if 'username' in form.errors:
                messages.error(request, 'Username error: ' + ', '.join(form.errors['username']))
            if 'email' in form.errors:
                messages.error(request, 'Email error: ' + ', '.join(form.errors['email']))
            if 'password1' in form.errors:
                messages.error(request, 'Password error: ' + ', '.join(form.errors['password1']))
            if 'password2' in form.errors:
                messages.error(request, 'Password confirmation error: ' + ', '.join(form.errors['password2']))
            # Add more specific error messages as needed
            messages.error(request, 'Registration failed. Please check the form and try again.')

    context = {'form': form}
    return render(request, 'base/login_register.html', context)
