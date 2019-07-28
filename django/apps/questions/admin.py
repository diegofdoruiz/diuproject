from django.contrib import admin

# Register your models here.
from .models import Question, Answer # Importamos todos los objetos de nuestra aplicación

# Register your models here.
admin.site.register(Question) # Registramos el objeto Pregunta
admin.site.register(Answer) # Registramos el objeto Respuesta