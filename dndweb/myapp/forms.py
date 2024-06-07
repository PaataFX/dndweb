from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

User = get_user_model()  # Retrieve the custom user model

class CustomUserUpdateForm(UserChangeForm):
    email = forms.EmailField(label="იმეილი", required=True)

    class Meta:
        model = User  # Use the custom user model
        fields = ('username', 'email')  # Specify the fields you want to be editable

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        self.fields['username'].label = "სახელი"
        self.fields['email'].label = "იმეილი"
        del self.fields['password']  # Remove password fields from the form

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label="სახელი", help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.")
    email = forms.EmailField(label="იმეილი")
    password1 = forms.CharField(label="პაროლი", widget=forms.PasswordInput, help_text="Your password can’t be too similar to your other personal information. Your password must contain at least 8 characters. Your password can’t be a commonly used password. Your password can’t be entirely numeric.")
    password2 = forms.CharField(label="გაიმეორე პაროლი", widget=forms.PasswordInput, help_text="Enter the same password as before, for verification.")

    class Meta:
        model = User  # Use the custom user model
        fields = ['username', 'email', 'password1', 'password2']