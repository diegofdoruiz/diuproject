from apps.questions.models import *
from django import forms

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = (
            'id',
            'name',
            'option')
        widgets = {
        }
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            'id',
            'name',
        	'question',
            'answers',
            'video')
        widgets = {
            'answers': forms.CheckboxSelectMultiple()
        }