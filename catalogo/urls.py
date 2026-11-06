from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('chefs', views.ChefViewSet)

urlpatterns = [
    path('platos/', views.plato_list, name='plato_list'),
    path('categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
]

urlpatterns += router.urls