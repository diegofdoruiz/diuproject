from django.db import models
from apps.courses.models import Course
from apps.topics.models import Topic

class Game(models.Model):
	name = models.CharField(max_length=128, null=False, blank=False)
	description = models.CharField(max_length=512, null=True, blank=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
	topics = models.ManyToManyField(Topic)
	completed = models.BooleanField(default=False)
	current = models.BooleanField(default=False)
	arduino_task_id = models.CharField(max_length=256, null=True)
	waiting_topic = models.BooleanField(default=False)
	waiting_answer = models.BooleanField(default=False)
	reading_topic = models.BooleanField(default=False)
	reading_question = models.BooleanField(default=False)
	channel = models.CharField(max_length=64, null=True, blank=True)
	user_id = models.CharField(max_length=10, null=True, blank=True)

	def __str__(self):
		return self.name