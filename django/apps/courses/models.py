from django.db import models
from apps.users.models import User

class Course(models.Model):
	name = models.CharField(max_length=128, null=False, blank=False)
	description = models.CharField(max_length=512, null=True, blank=True)
	teachers = models.ManyToManyField(User, related_name='teachers')
	students = models.ManyToManyField(User)

	def __str__(self):
		return self.name