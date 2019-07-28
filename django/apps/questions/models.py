from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=100)
    video = models.CharField(blank=False, max_length=500)
class Answer(models.Model):
	question = models.ForeignKey('Question', on_delete='') # Campo con que se relaciona la pregunta de esta respuesta
	option = models.CharField(max_length=200) # Campo tipo Char con un máximo de 200 caracteres de longitud.
    