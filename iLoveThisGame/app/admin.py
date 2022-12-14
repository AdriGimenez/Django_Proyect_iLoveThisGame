from django.contrib import admin

# Register your models here.

from app.models import Categoria, Articulo
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Articulo)