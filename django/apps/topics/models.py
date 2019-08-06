from django.db import models
from django.core.validators import MinLengthValidator
from apps.questions.models import Question   

class Topic(models.Model): 
    name = models.CharField(max_length=20, validators=[MinLengthValidator(6, 'Mínimo 6 carateres.')])
    info = models.TextField(validators=[MinLengthValidator(6, 'Mínimo 6 carateres.')])
    card = models.CharField(max_length=128, null=False, blank=False)
    questions = models.ManyToManyField(Question)

    def __str__(self):
    	return self.name
