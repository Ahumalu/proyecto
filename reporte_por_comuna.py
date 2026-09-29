import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')
django.setup()

from django.db import connection
from gestion_inmuebles.models import Comuna, Inmueble


def generar_reporte():
    with open('reporte_inmuebles_por_comuna.txt', 'w', encoding='utf-8') as archivo:

        # ---------- PARTE 1: usando el ORM de Django ----------
        archivo.write("=== LISTADO DE INMUEBLES POR COMUNA (usando ORM de Django) ===\n\n")

        comunas = Comuna.objects.all().order_by('nombre')
        for comuna in comunas:
            inmuebles = Inmueble.objects.filter(comuna=comuna).values('nombre', 'descripcion')
            if inmuebles:
                archivo.write(f"Comuna: {comuna.nombre}\n")
                for inmueble in inmuebles:
                    archivo.write(f"  - Nombre: {inmueble['nombre']}\n")
                    archivo.write(f"    Descripción: {inmueble['descripcion']}\n")
                archivo.write("\n")

        # ---------- PARTE 2: usando SQL directo ----------
        archivo.write("\n=== LISTADO DE INMUEBLES POR COMUNA (usando SQL directo) ===\n\n")

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT c.nombre AS comuna, i.nombre AS inmueble, i.descripcion
                FROM gestion_inmuebles_inmueble i
                JOIN gestion_inmuebles_comuna c ON i.comuna_id = c.id
                ORDER BY c.nombre;
            """)
            filas = cursor.fetchall()

            comuna_actual = None
            for comuna_nombre, inmueble_nombre, descripcion in filas:
                if comuna_nombre != comuna_actual:
                    archivo.write(f"Comuna: {comuna_nombre}\n")
                    comuna_actual = comuna_nombre
                archivo.write(f"  - Nombre: {inmueble_nombre}\n")
                archivo.write(f"    Descripción: {descripcion}\n")

    print("Reporte generado en 'reporte_inmuebles_por_comuna.txt'")


if __name__ == '__main__':
    generar_reporte()