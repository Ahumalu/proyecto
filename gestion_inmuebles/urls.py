from django.urls import path
from django.contrib.auth import views as auth_views
from .views import registro, perfil, crear_inmueble, editar_inmueble, borrar_inmueble, listado_inmuebles

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='gestion_inmuebles/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='gestion_inmuebles/logout.html'), name='logout'),
    path('register/', registro, name='register'),
    path('perfil/', perfil, name='perfil'),
    path('inmuebles/nuevo/', crear_inmueble, name='crear_inmueble'),
    path('inmuebles/<int:inmueble_id>/editar/', editar_inmueble, name='editar_inmueble'),
    path('inmuebles/<int:inmueble_id>/borrar/', borrar_inmueble, name='borrar_inmueble'),
    path('inmuebles/', listado_inmuebles, name='listado_inmuebles'),
]