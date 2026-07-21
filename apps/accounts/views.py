from django.contrib import messages
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, RegistrationForm
from .models import User


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Account created successfully. Please log in.")
        return response


class LoginView(DjangoLoginView):
    authentication_form = LoginForm
    template_name = "accounts/login.html"

    def form_valid(self, form):
        messages.success(self.request, f"Welcome back, {form.get_user().username}!")
        return super().form_valid(form)


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("accounts:login")
