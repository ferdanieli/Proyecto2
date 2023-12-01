from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from accounts.forms import UserRegisterForm


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)


        return redirect('CursoList')

    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/login.html", contexto)

def register_request(request):
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("CursoList")

    # form = UserCreationForm()
    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)
