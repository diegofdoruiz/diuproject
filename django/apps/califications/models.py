from django.db import models
from apps.users.models import User
from apps.games.models import Game
# Create your models here.
class Calification(models.Model):
	note = models.DecimalField(max_digits=5, decimal_places=2)
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)

	def __str__(self):
		return self.name