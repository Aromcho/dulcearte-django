from django.db import models
from django.conf import settings

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Publicacion(models.Model):
    contenido = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    contenido = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='comentarios', default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
class MeGusta(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, related_name='megusta_set', on_delete=models.CASCADE, default=1)  # Cambia '1' por el ID de una receta válida
    fecha_creacion = models.DateTimeField(auto_now_add=True)