from django.db import models

class Question(models.Model):
	name = models.CharField(max_length=512, null=False, blank=False)
	statement = models.TextField(null=False, blank=False)
	answer_1 = models.CharField(max_length=512, null=True, blank=True)
	answer_2 = models.CharField(max_length=512, null=True, blank=True)
	answer_3 = models.CharField(max_length=512, null=True, blank=True)
	answer_4 = models.CharField(max_length=512, null=True, blank=True)
	answer_5 = models.CharField(max_length=512, null=True, blank=True)
	correct_answer = models.CharField(max_length=32, null=False, blank=False)
	video = models.CharField(blank=False, max_length=500)
	def __str__(self):
		return self.name
    