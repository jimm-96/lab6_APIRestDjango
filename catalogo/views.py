from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Datos de ejemplo en memoria para el recurso Plato
platos = [
    {
        "id": 1,
        "nombre": "Pastel de Choclo",
        "precio": 8500,
        "categoria": "Fondos",
        "disponible": True
    },
    {
        "id": 2,
        "nombre": "Ceviche Mixto",
        "precio": 9200,
        "categoria": "Entradas",
        "disponible": True
    },
    {
        "id": 3,
        "nombre": "Tiramisú Artesanal",
        "precio": 4500,
        "categoria": "Postres",
        "disponible": False
    }
]


@api_view(['GET'])
def plato_list(request):
    """
    Endpoint para obtener la lista de platos (GET).
    """
    if request.method == 'GET':
        return Response(platos)
