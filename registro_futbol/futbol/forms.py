from django import forms
from .models import Jugador, Equipo

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'edad', 'posicion', 'pais', 'equipo', 'foto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'posicion': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'equipo': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'pais', 'entrenador', 'escudo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'entrenador': forms.TextInput(attrs={'class': 'form-control'}),
            'escudo': forms.FileInput(attrs={'class': 'form-control'}),
        }