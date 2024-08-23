from django.contrib import admin
from .models import Receta, Publicacion, Comentario, MeGusta

admin.site.register(Receta)
admin.site.register(Publicacion)
admin.site.register(Comentario)
admin.site.register(MeGusta)

