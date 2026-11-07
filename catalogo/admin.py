from django.contrib import admin

from .models import Categoria, Chef, Plato

admin.site.register(Plato)
admin.site.register(Chef)
admin.site.register(Categoria)
