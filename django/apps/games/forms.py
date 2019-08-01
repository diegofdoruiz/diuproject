from django import forms
from apps.games.models import Game
from apps.questions.models import Question
from apps.courses.models import Course
from django_select2.forms import Select2MultipleWidget


class GameForm(forms.ModelForm):

	# def __init__(self, *args, **kwargs):
	# 	super(GameForm, self).__init__(*args, **kwargs)
	# 	self.fields['course'].queryset = Course.objects.all()
		
	class Meta:
		model = Game
		fields = (
			'id',
			'name',
			'description',
			'course',
			'questions'
		)
		widgets= {
			'id' : forms.TextInput(attrs={'class':'form-control'}),
			'name' : forms.TextInput(attrs={'class':'form-control'}),
			'description' : forms.TextInput(attrs={'class':'form-control'}),
			'questions' :forms.CheckboxSelectMultiple(),
			'course' : forms.CheckboxSelectMultiple(),
		}