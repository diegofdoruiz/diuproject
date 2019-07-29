from django.db import models

class Answer(models.Model):
	name = models.CharField(max_length=128, null=False, blank=False)
	option = models.CharField(max_length=256) # Campo tipo Char con un máximo de 200 caracteres de longitud.

	def __str__(self):
		return self.name

class Question(models.Model):
	name = models.CharField(max_length=128, null=False, blank=False)
	question = models.CharField(max_length=512)
	answers = models.ManyToManyField(Answer)
	video = models.CharField(blank=False, max_length=500)
	def __str__(self):
		return self.name
    