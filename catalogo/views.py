from django.shortcuts import render

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
