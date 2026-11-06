from django.urls import path
from . import views

urlpatterns = [
    path('platos/', views.plato_list, name='plato_list'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
]

