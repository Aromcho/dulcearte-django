from django.shortcuts import render
from .forms import RecetaForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import PublicacionForm
from .forms import ComentarioForm
from .models import Publicacion
from .models import MeGusta
from .models import Receta
from django.db import IntegrityError




def home(request):
    recetas = Receta.objects.all().order_by('-fecha_creacion')[:6]  # Muestra las 6 recetas más recientes
    return render(request, 'recetas/home.html', {'recetas': recetas})

@login_required
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            receta = form.save(commit=False)
            receta.autor = request.user  # Asigna el usuario autenticado como autor
            receta.save()
            return redirect('home')
    else:
        form = RecetaForm()
    return render(request, 'recetas/crear_receta.html', {'form': form})


@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('home')
    else:
        form = PublicacionForm()
    return render(request, 'recetas/crear_publicacion.html', {'form': form})

@login_required
def agregar_comentario(request, publicacion_id):
    publicacion = Publicacion.objects.get(id=publicacion_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.publicacion = publicacion
            comentario.save()
            return redirect('home')
    else:
        form = ComentarioForm()
    return render(request, 'recetas/agregar_comentario.html', {'form': form, 'publicacion': publicacion})

@login_required
def dar_megusta(request, publicacion_id):
    publicacion = Publicacion.objects.get(id=publicacion_id)
    MeGusta.objects.create(usuario=request.user, publicacion=publicacion)
    return redirect('home')
