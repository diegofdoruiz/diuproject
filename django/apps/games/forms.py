from django import forms
from apps.games.models import Game
from apps.questions.models import Question
from apps.courses.models import Course


class GameForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(GameForm, self).__init__(*args, **kwargs)
		self.fields['course'].queryset = Course.objects.all()
		
	class Meta:
		model = Game
		fields = (
			'id',
			'name',
			'description',
			'course',
			'topics'
		)
