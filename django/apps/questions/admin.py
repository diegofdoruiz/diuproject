from django.contrib import admin

# Register your models here.
from .models import Question # Importamos todos los objetos de nuestra aplicación

# Register your models here.
admin.site.register(Question) # Registramos el objeto Pregunta
