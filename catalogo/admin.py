# Register your models here.

from django.contrib import admin
from .models import Categoria, Chef

admin.site.register(Chef)
admin.site.register(Categoria)
