from apps.questions.models import *
from django import forms
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            'id',
            'name',
<<<<<<< HEAD
        	'question',
            'answers',
            'video')
        widgets = {
            'answers': forms.CheckboxSelectMultiple()
=======
        	'statement',
            'video',
            'answer_1',
            'answer_2',
            'answer_3',
            'answer_4',
            'answer_5',
            'correct_answer')
        labels = {
            'name':'Nombre',
            'statement':'Enunciado',
            'video':'Multimedia',
>>>>>>> 37eeb2a5b989a3becbb94106732ad835cf3831ac
        }