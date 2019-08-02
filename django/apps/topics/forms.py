from django import forms
from apps.topics.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = (
        	'name',
            'info',
            'card',
            'questions') 
        labels=  {
        'name': 'Nombre de Personaje',
        'info': 'Información de Personaje',
        'card': 'Tarjeta que representa este tema',
        'questions': 'Preguntas asociadas este tema',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'info': forms.TextInput(attrs={'class':'form-control'})
        }