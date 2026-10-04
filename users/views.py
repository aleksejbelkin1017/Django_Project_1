from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView as BaseLoginView,
    LogoutView as BaseLogoutView,
)
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView

from users.forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    UserProfileForm,
)
from users.models import User


class RegisterView(FormView):
    # Регистрация: создание пользователя + авто-вход + приветственное письмо
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        # Вызывается только если форма прошла валидацию
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        # fail_silently=True — падение почты не сломает регистрацию
        send_mail(
            subject="Добро пожаловать в наш сервис",
            message="Спасибо, что зарегистрировались в нашем сервисе!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user_email],
            fail_silently=True,
        )


class LoginView(BaseLoginView):
    # Вход по email (кастомная форма)
    form_class = CustomAuthenticationForm
    template_name = "users/login.html"


class LogoutView(BaseLogoutView):
    # Куда редиректить после выхода
    next_page = reverse_lazy("catalog:products_list")


class ProfileView(LoginRequiredMixin, UpdateView):
    # Редактирование своего профиля (доп. задание)
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        # Возвращаем самого пользователя, а не объект по pk
        return self.request.user