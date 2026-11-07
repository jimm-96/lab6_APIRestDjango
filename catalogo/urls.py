from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('platos', views.PlatoViewSet)
router.register('chefs', views.ChefViewSet)
router.register('categorias', views.CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
