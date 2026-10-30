from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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


@api_view(['GET', 'POST'])
def plato_list(request):
    """
    Endpoint para listar platos (GET) y agregar un nuevo plato (POST).
    """
    if request.method == 'GET':
        return Response(platos)

    elif request.method == 'POST':
        nombre = request.data.get('nombre')
        precio = request.data.get('precio')

        if not nombre or precio is None:
            return Response(
                {"error": "Los campos 'nombre' y 'precio' son requeridos."},
                status=status.HTTP_400_BAD_REQUEST
            )

        nuevo_id = (max([p["id"] for p in platos]) + 1) if platos else 1
        nuevo_plato = {
            "id": nuevo_id,
            "nombre": nombre,
            "precio": precio,
            "categoria": request.data.get('categoria', 'General'),
            "disponible": request.data.get('disponible', True)
        }
        platos.append(nuevo_plato)
        return Response(nuevo_plato, status=status.HTTP_201_CREATED)
