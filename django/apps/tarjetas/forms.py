from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.tarjetas.models import Personaje, Tarjeta


class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = (
        	'nombre_personaje',
            'info_personaje') 
        labels=  {
        'nombre_personaje': 'Nombre de Personaje',
        'info_personaje': 'Información de Personaje',
        }
        widgets = {
            'nombre_personaje': forms.TextInput(attrs={'class':'form-control'}),
            'info_personaje': forms.TextInput(attrs={'class':'form-control'})

        }