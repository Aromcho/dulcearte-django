from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta básica para la vista 'home'
    path('crear/', views.crear_receta, name='crear_receta'),
    path('crear_publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('publicacion/<int:publicacion_id>/comentario/', views.agregar_comentario, name='agregar_comentario'),
    path('publicacion/<int:publicacion_id>/megusta/', views.dar_megusta, name='dar_megusta'),
    
    # Nuevas rutas
    path('receta/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),  # Detalle de receta
    path('mis_recetas/', views.mis_recetas, name='mis_recetas'),
    path('admin/', views.admin_page, name='admin'),
    path('feed/', views.feed, name='feed'),
     path('receta/<int:receta_id>/megusta/', views.dar_megusta, name='dar_megusta'),
    path('receta/<int:receta_id>/comentario/', views.agregar_comentario, name='agregar_comentario'),
]
