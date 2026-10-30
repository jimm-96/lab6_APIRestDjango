from django.shortcuts import render

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
