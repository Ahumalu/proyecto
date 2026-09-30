# 🏠 Proyecto Arriendo de Inmuebles

Sitio web desarrollado con **Django** y **PostgreSQL**, que permite a una empresa de arriendo de inmuebles publicar y gestionar propiedades disponibles, separadas por comuna y región.

Proyecto desarrollado de forma incremental a lo largo de distintos hitos del bootcamp de Desafío Latam.

## ✨ Características

- Panel de administración de Django personalizado (registro de modelos, filtros y búsqueda).
- Autenticación de usuarios (registro, login y logout) con `django.contrib.auth`.
- Modelo de datos con Región, Comuna, Tipo de Inmueble, Usuario e Inmueble.
- Perfil de usuario editable, vinculado a su cuenta de autenticación.
- CRUD completo de inmuebles (crear, editar, eliminar y listar), con validación de permisos según el tipo de usuario (arrendador o arrendatario).
- Filtrado del listado de inmuebles por región y comuna.
- Scripts en Python (`reporte_por_comuna.py`, `reporte_por_region.py`) que consultan la base de datos usando el ORM de Django y SQL directo, generando reportes en archivos de texto.

## 🛠️ Tecnologías utilizadas

- Python
- Django
- PostgreSQL

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio: git clone https://github.com/Ahumalu/proyecto.git

2. Crea y activa un entorno virtual, e instala Django y psycopg2.
3. Configura una base de datos PostgreSQL y actualiza los datos de conexión en `proyecto_inmuebles/settings.py`.
4. Aplica las migraciones: python manage.py migrate
5. 5. Levanta el servidor: python manage.py runserver
