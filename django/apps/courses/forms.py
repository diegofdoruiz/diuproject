from django import forms
from apps.courses.models import Course
from apps.users.models import User

class CourseForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(CourseForm, self).__init__(*args, **kwargs)
		self.fields['teachers'].queryset = User.objects.filter(groups__name='docente')
		self.fields['students'].queryset = User.objects.filter(groups__name='estudiante')

	class Meta:
		model = Course
		fields = (
			'id',
			'name',
			'description',
			'teachers',
			'students'
		)