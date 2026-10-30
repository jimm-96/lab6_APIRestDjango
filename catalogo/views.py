from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


# ===== CATEGORIA =====
categorias = [
    {
        "id": 1,
        "nombre": "Entradas",
        "descripcion": "Platos pequeños para comenzar la comida",
        "activa": True,
    },
    {
        "id": 2,
        "nombre": "Platos de fondo",
        "descripcion": "Platos principales del restaurante",
        "activa": True,
    },
    {
        "id": 3,
        "nombre": "Postres",
        "descripcion": "Dulces para cerrar la comida",
        "activa": True,
    },
]


@api_view(['GET'])
def listar_categorias(request):
    return Response(categorias)


@api_view(['POST'])
def crear_categoria(request):
    nombre = request.data.get("nombre")
    if not nombre:
        return Response(
            {"error": "El campo 'nombre' es obligatorio"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    nuevo_id = max((c["id"] for c in categorias), default=0) + 1
    nueva_categoria = {
        "id": nuevo_id,
        "nombre": nombre,
        "descripcion": request.data.get("descripcion", ""),
        "activa": request.data.get("activa", True),
    }
    categorias.append(nueva_categoria)
    return Response(nueva_categoria, status=status.HTTP_201_CREATED)
