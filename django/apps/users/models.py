from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator

class User(AbstractUser):
    id_card = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(8, 'Mínimo 8 dígitos')])
    address = models.CharField(max_length=50)
    birthday = models.DateField(null=True)
    phone = models.CharField(max_length=11)

    def __str__(self):
    	return self.get_full_name()
