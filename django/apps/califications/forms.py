from apps.califications.models import *
from django import forms
        
class CalificationForm(forms.ModelForm):
    class Meta:
        model = Calification
        fields = (
            'note',
            'student',
        	'game',)
        labels = {
            'note':'Nota',
            'student':'Estudiante',
            'game':'Partida',
        };