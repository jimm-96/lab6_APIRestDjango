from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'platos', views.PlatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('chefs/', views.lista_chefs, name='lista_chefs'),
    path('chefs/crear/', views.crear_chef, name='crear_chef'),
]

