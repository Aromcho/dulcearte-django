from django.shortcuts import render, get_object_or_404
from .forms import RecetaForm, PublicacionForm, ComentarioForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Receta, Publicacion, MeGusta, Comentario
from django.contrib import messages
from django.http import JsonResponse


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
def agregar_comentario(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            comentario = Comentario.objects.create(contenido=contenido, autor=request.user, receta=receta)
            return JsonResponse({
                'comentario': comentario.contenido,
                'autor': comentario.autor.username  # O cualquier otro dato del autor que quieras mostrar
            })


@login_required
def dar_megusta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    # Crear un nuevo 'Me gusta' si no existe
    MeGusta.objects.create(usuario=request.user, receta=receta)
    return JsonResponse({'likes': receta.megusta_set.count()})

@login_required
def mis_recetas(request):
    recetas = Receta.objects.filter(autor=request.user)  # Muestra solo las recetas del usuario autenticado
    return render(request, 'recetas/mis_recetas.html', {'recetas': recetas})

@login_required
def admin_page(request):
    # Aquí puedes agregar lógica específica para la página del admin
    return render(request, 'recetas/admin.html')

def feed(request):
    recetas = Receta.objects.all().order_by('-fecha_creacion')
    return render(request, 'recetas/feed.html', {'recetas': recetas})

@login_required
def dar_megusta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if not MeGusta.objects.filter(usuario=request.user, receta=receta).exists():
        MeGusta.objects.create(usuario=request.user, receta=receta)
    return redirect('detalle_receta', receta_id=receta.id)   # Redirigimos de nuevo al feed

@login_required
def agregar_comentario(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            Comentario.objects.create(contenido=contenido, autor=request.user, receta=receta)
            messages.success(request, 'Comentario agregado exitosamente')
    return redirect('detalle_receta', receta_id=receta_id) # Asegúrate de que la redirección sea a la página correcta

def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)

    # Si el método es POST, intentamos publicar la receta
    if request.method == 'POST' and 'publicar' in request.POST:
        receta.publicada = True  # Cambiamos el estado de la receta a publicada
        receta.save()
        # Redirigimos a la página actual para ver la receta actualizada
        return redirect('detalle_receta', receta_id=receta.id)

    return render(request, 'recetas/detalle_receta.html', {'receta': receta})
