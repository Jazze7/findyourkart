from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
# from posts.models import Author


# from users.forms import UserForm
# from main.functions import generate_form_errors

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)

                return HttpResponseRedirect("/")

        context = {
            "title": "Login",
            "error": True,
            "message": "Invalid username or password"
        }
        return render(request, "users/login.html", context)
    else:
        context = {
            "title": "Login",

        }
        return render(request, "users/login.html", context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:index"))
