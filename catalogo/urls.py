from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('chefs', views.ChefViewSet)
router.register('categorias', views.CategoriaViewSet)

urlpatterns = [
    path('platos/', views.plato_list, name='plato_list'),
]

urlpatterns += router.urls