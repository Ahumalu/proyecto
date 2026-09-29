import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')
django.setup()

from django.db import connection
from gestion_inmuebles.models import Region, Inmueble


def generar_reporte():
    with open('reporte_inmuebles_por_region.txt', 'w', encoding='utf-8') as archivo:

        # ---------- PARTE 1: usando el ORM de Django ----------
        archivo.write("=== LISTADO DE INMUEBLES POR REGIÓN (usando ORM de Django) ===\n\n")

        regiones = Region.objects.all().order_by('nombre')
        for region in regiones:
            inmuebles = Inmueble.objects.filter(comuna__region=region).values('nombre', 'descripcion')
            if inmuebles:
                archivo.write(f"Región: {region.nombre}\n")
                for inmueble in inmuebles:
                    archivo.write(f"  - Nombre: {inmueble['nombre']}\n")
                    archivo.write(f"    Descripción: {inmueble['descripcion']}\n")
                archivo.write("\n")

        # ---------- PARTE 2: usando SQL directo ----------
        archivo.write("\n=== LISTADO DE INMUEBLES POR REGIÓN (usando SQL directo) ===\n\n")

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT r.nombre AS region, i.nombre AS inmueble, i.descripcion
                FROM gestion_inmuebles_inmueble i
                JOIN gestion_inmuebles_comuna c ON i.comuna_id = c.id
                JOIN gestion_inmuebles_region r ON c.region_id = r.id
                ORDER BY r.nombre;
            """)
            filas = cursor.fetchall()

            region_actual = None
            for region_nombre, inmueble_nombre, descripcion in filas:
                if region_nombre != region_actual:
                    archivo.write(f"Región: {region_nombre}\n")
                    region_actual = region_nombre
                archivo.write(f"  - Nombre: {inmueble_nombre}\n")
                archivo.write(f"    Descripción: {descripcion}\n")

    print("Reporte generado en 'reporte_inmuebles_por_region.txt'")


if __name__ == '__main__':
    generar_reporte()