from django.db import models
from django.core.validators import MinLengthValidator   
# Create your models here.

class Personaje(models.Model): 
    
    nombre_personaje= models.CharField(max_length=20, validators=[MinLengthValidator(6, 'Mínimo 6 carateres.')])
    info_personaje= models.TextField(max_length= 200, validators=[MinLengthValidator(6, 'Mínimo 6 carateres.')])
    ##TODO: Agregar las preguntas asociadas al personaje y audios


class Tarjeta(models.Model): 
    frecuencia = models.CharField(max_length=10,validators=[MinLengthValidator(5, 'Mínimo 8 dígitos.')] )
    personaje = models.ForeignKey(Personaje, null=False, blank=False, on_delete=models.CASCADE)

