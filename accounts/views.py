from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.decorators import account_ownership_required
from accounts.forms import SignupForm, UpdateForm

has_ownership = [
    account_ownership_required,
    login_required,
]


class AccountCreateView(CreateView):
    model = get_user_model()
    form_class = SignupForm
    success_url = reverse_lazy("index")
    template_name = "accounts/signup.html"


class AccountLoginView(LoginView):
    template_name = "accounts/signin.html"


class AccountLogoutView(LogoutView):
    pass


class AccountDetailView(DetailView):
    model = get_user_model()
    template_name = "accounts/detail.html"


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
@method_decorator(account_ownership_required, "get")
@method_decorator(account_ownership_required, "post")
class AccountUpdateView(UpdateView):
    model = get_user_model()
    form_class = UpdateForm
    success_url = reverse_lazy("index")
    template_name = "accounts/update.html"


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class AccountDeleteView(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy("index")
    template_name = "accounts/delete.html"
