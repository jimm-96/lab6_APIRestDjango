from django.urls import path
from . import views

urlpatterns = [
    path('platos/', views.plato_list, name='plato_list'),
]

