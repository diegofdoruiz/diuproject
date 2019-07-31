from django.db import models
from apps.courses.models import Course
from apps.questions.models import Question

class Game(models.Model):
	name = models.CharField(max_length=128, null=False, blank=False)
	description = models.CharField(max_length=512, null=True, blank=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
	questions = models.ManyToManyField(Question)

	def __str__(self):
		return self.name