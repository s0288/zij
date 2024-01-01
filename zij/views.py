from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import UserForm


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # hash password
            user.save()  # update with Hashed password
            login(request, user)
            messages.info(
                request,
                """
                          Welcome! Nice to have you around.""",
            )
            return redirect("/feedback/")
        else:
            messages.info(request, user_form.errors)
            return redirect("index")
    else:
        user_form = UserForm()  # just render the forms as blank.
    return render(request, "register.html", {"user_form": user_form})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("feedback:index"))
            else:
                messages.info(request, "Your account is not active.")
                return redirect("index")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            messages.info(request, "Invalid login details supplied.")
            return redirect("index")
    else:
        return render(request, "login.html", {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def why(request):
    return render(request, "why.html")
