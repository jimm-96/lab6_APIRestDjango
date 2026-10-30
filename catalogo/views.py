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

# Create your views here.

CHEFS = [
    {"id": 1, "nombre": "Camila Rojas", "especialidad": "Cocina chilena", "anios_experiencia": 12},
    {"id": 2, "nombre": "Matías Soto", "especialidad": "Pastelería", "anios_experiencia": 8},
    {"id": 3, "nombre": "Valentina Díaz", "especialidad": "Cocina italiana", "anios_experiencia": 5},
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
def lista_chefs(request):
    return Response(CHEFS)


@api_view(['POST'])
def crear_chef(request):
    nuevo_id = max((c["id"] for c in CHEFS), default=0) + 1
    chef = {
        "id": nuevo_id,
        "nombre": request.data.get("nombre"),
        "especialidad": request.data.get("especialidad"),
        "anios_experiencia": request.data.get("anios_experiencia"),
    }
    CHEFS.append(chef)
    return Response(chef, status=201)
