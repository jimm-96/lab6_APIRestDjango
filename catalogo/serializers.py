from rest_framework import serializers
from .models import Categoria, Chef


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
