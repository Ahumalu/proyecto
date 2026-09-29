from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, EditarPerfilForm, InmuebleForm
from .models import Inmueble


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'gestion_inmuebles/register.html', {'form': form})


@login_required
def perfil(request):
    usuario = getattr(request.user, 'usuario', None)

    if usuario is None:
        return render(request, 'gestion_inmuebles/perfil.html', {'usuario': None})

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditarPerfilForm(instance=usuario)

    mis_inmuebles = usuario.inmuebles.all() if usuario.tipo_usuario == 'arrendador' else None

    return render(request, 'gestion_inmuebles/perfil.html', {
        'usuario': usuario,
        'form': form,
        'mis_inmuebles': mis_inmuebles,
    })


@login_required
def crear_inmueble(request):
    usuario = getattr(request.user, 'usuario', None)

    if usuario is None or usuario.tipo_usuario != 'arrendador':
        return render(request, 'gestion_inmuebles/sin_permiso.html')

    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = form.save(commit=False)
            inmueble.arrendador = usuario
            inmueble.save()
            return redirect('perfil')
    else:
        form = InmuebleForm()

    return render(request, 'gestion_inmuebles/inmueble_form.html', {'form': form})


@login_required
def editar_inmueble(request, inmueble_id):
    usuario = getattr(request.user, 'usuario', None)
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)

    if usuario is None or usuario.tipo_usuario != 'arrendador' or inmueble.arrendador != usuario:
        return render(request, 'gestion_inmuebles/sin_permiso.html')

    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = InmuebleForm(instance=inmueble)

    return render(request, 'gestion_inmuebles/inmueble_form.html', {'form': form, 'editar': True})


@login_required
def borrar_inmueble(request, inmueble_id):
    usuario = getattr(request.user, 'usuario', None)
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)

    if usuario is None or usuario.tipo_usuario != 'arrendador' or inmueble.arrendador != usuario:
        return render(request, 'gestion_inmuebles/sin_permiso.html')

    if request.method == 'POST':
        inmueble.delete()
        return redirect('perfil')

    return render(request, 'gestion_inmuebles/inmueble_confirmar_borrado.html', {'inmueble': inmueble})


@login_required
def listado_inmuebles(request):
    inmuebles = Inmueble.objects.all().order_by('comuna__nombre')
    return render(request, 'gestion_inmuebles/listado_inmuebles.html', {'inmuebles': inmuebles})