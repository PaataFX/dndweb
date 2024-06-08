from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

User = get_user_model()

class CustomUserUpdateForm(UserChangeForm):
    email = forms.EmailField(label="იმეილი", required=True)
    avatar = forms.ImageField(label="Avatar", required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        self.fields['username'].label = "სახელი"
        self.fields['email'].label = "იმეილი"
        del self.fields['password']

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label="სახელი", help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    email = forms.EmailField(label="იმეილი")
    password1 = forms.CharField(label="პაროლი", widget=forms.PasswordInput, help_text="Your password can’t be too similar to your other personal information. Your password must contain at least 8 characters. Your password can’t be a commonly used password. Your password can’t be entirely numeric.")
    password2 = forms.CharField(label="გაიმეორე პაროლი", widget=forms.PasswordInput, help_text="Enter the same password as before, for verification.")

    class Meta:
        model = User  # Use the custom user model
        fields = ['username', 'email', 'password1', 'password2']
        

from .models import Character

class CustomCharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name', 'race', 'subrace', 'dnd_class', 'subclass', 'level', 'alignment', 'background', 
            'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma'
        ]
        
    def __init__(self, *args, **kwargs):
        super(CustomCharacterForm, self).__init__(*args, **kwargs)
        # Set fields as optional
        self.fields['subrace'].required = False
        self.fields['subclass'].required = False
        self.fields['alignment'].required = False
        self.fields['background'].required = False
        self.fields['level'].required = False
