from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from .models import Categoria, Chef
from .serializers import CategoriaSerializer, ChefSerializer
# Create your views here.

from django.http import Http404

from rest_framework import viewsets

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

# CHEFS = [
#     {"id": 1, "nombre": "Camila Rojas", "especialidad": "Cocina chilena", "anios_experiencia": 12},
#     {"id": 2, "nombre": "Matías Soto", "especialidad": "Pastelería", "anios_experiencia": 8},
#     {"id": 3, "nombre": "Valentina Díaz", "especialidad": "Cocina italiana", "anios_experiencia": 5},
# ]



# ===== CATEGORIA =====
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


# Version anterior del CRUD con APIView (Laboratorio 7)
# class CategoriaList(APIView):
#     def get(self, request):
#         categorias = Categoria.objects.all()
#         serializer = CategoriaSerializer(categorias, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = CategoriaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CategoriaDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Categoria.objects.get(pk=pk)
#         except Categoria.DoesNotExist:
#             raise Http404
#
#     def put(self, request, pk):
#         categoria = self.get_object(pk)
#         serializer = CategoriaSerializer(categoria, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         categoria = self.get_object(pk)
#         categoria.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def lista_chefs(request):
#     return Response(CHEFS)


# @api_view(['POST'])
# def crear_chef(request):
#     nuevo_id = max((c["id"] for c in CHEFS), default=0) + 1
#     chef = {
#         "id": nuevo_id,
#         "nombre": request.data.get("nombre"),
#         "especialidad": request.data.get("especialidad"),
#         "anios_experiencia": request.data.get("anios_experiencia"),
#     }
#     CHEFS.append(chef)
#     return Response(chef, status=201)


#lab 7
# class ChefList(APIView):
#     def get(self, request):
#         return Response(ChefSerializer(Chef.objects.all(), many=True).data)

#     def post(self, request):
#         serializer = ChefSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# class ChefDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Chef.objects.get(pk=pk)
#         except Chef.DoesNotExist:
#             raise Http404

#     def put(self, request, pk):
#         serializer = ChefSerializer(self.get_object(pk), data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     def delete(self, request, pk):
#         self.get_object(pk).delete()
#         return Response(status=204)


class ChefViewSet(viewsets.ModelViewSet):
    queryset = Chef.objects.all()
    serializer_class = ChefSerializer