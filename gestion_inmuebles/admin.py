from django.contrib import admin
from .models import Inmueble, Region, Comuna

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'comuna', 'precio_mensual', 'tipo_inmueble')
    search_fields = ('nombre', 'direccion')
    list_filter = ('tipo_inmueble', 'comuna')

admin.site.register(Region)
admin.site.register(Comuna)