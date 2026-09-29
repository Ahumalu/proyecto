from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario, Inmueble


class RegistroForm(UserCreationForm):
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=12)
    direccion = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=20)
    correo = forms.EmailField()
    tipo_usuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            Usuario.objects.create(
                user=user,
                nombres=self.cleaned_data['nombres'],
                apellidos=self.cleaned_data['apellidos'],
                rut=self.cleaned_data['rut'],
                direccion=self.cleaned_data['direccion'],
                telefono=self.cleaned_data['telefono'],
                correo=self.cleaned_data['correo'],
                tipo_usuario=self.cleaned_data['tipo_usuario'],
            )
        return user


class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellidos', 'rut', 'direccion', 'telefono', 'correo', 'tipo_usuario']


class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            'nombre', 'descripcion', 'm2_construidos', 'm2_totales',
            'estacionamientos', 'habitaciones', 'banos', 'direccion',
            'comuna', 'tipo_inmueble', 'precio_mensual',
        ]