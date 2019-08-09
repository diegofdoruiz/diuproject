from apps.califications.models import *
from django import forms
        
class CalificationForm(forms.ModelForm):
    class Meta:
        model = Calification
        fields = (
            'note',
            'student',
            'question',
        	'game',)
        labels = {
            'note':'Nota',
            'question':'Pregunta',
            'student':'Estudiante',
            'game':'Partida',
        };