from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Profile, User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data["email"].lower()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email exists.")
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "avatar",
            "bio",
            "phone_number",
            "job_title",
            "website",
            "facebook_url",
            "x_url",
            "linkedin_url",
            "instagram_url",
        )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
