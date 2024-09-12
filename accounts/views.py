from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
        ]


def registration(request):
    if request.method == "POST":
        form = CustomUserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("register")
    else:
        form = CustomUserCreateForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/register.html", context)


def home(request):
    # request.user.tasks.all()

    # Task.objects.filter(user=request.user)

    return render(request, "accounts/home.html")


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("accounts_home")
    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)
