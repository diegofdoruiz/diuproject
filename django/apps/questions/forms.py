from apps.questions.models import *
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
        	'question',
            'video')
        widgets = {
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = (
        	'question',
            'option')
        widgets = {
        }