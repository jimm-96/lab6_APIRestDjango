from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

CHEFS = [
    {"id": 1, "nombre": "Camila Rojas", "especialidad": "Cocina chilena", "anios_experiencia": 12},
    {"id": 2, "nombre": "Matías Soto", "especialidad": "Pastelería", "anios_experiencia": 8},
    {"id": 3, "nombre": "Valentina Díaz", "especialidad": "Cocina italiana", "anios_experiencia": 5},
]


@api_view(['GET'])
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
