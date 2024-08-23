from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout  
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("Usuario guardado:", user)
            login(request, user)
            return redirect('home')
        else:
            print("Formulario no válido:", form.errors)
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/inicio_sesion.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home')
