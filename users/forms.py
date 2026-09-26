from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class CustomUserCreationForm(UserCreationForm):
    """Форма регистрации: email + пароль + подтверждение пароля."""
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "password1", "password2")


class CustomAuthenticationForm(AuthenticationForm):
    """Форма входа: email вместо username."""
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"autofocus": True}),
    )


class UserProfileForm(forms.ModelForm):
    """Форма редактирования профиля (доп. задание)."""
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "avatar", "phone", "country")