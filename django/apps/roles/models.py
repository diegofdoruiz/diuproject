from django.db import models
from django.contrib.auth.models import Group, Permission

class Role(models.Model):
	name = models.CharField(max_length=100, null=False, blank=False)
	permission = models.ManyToManyField(Permission)
	@staticmethod
	def get_roles():
		try:
			queryset = Role.objects.all()
			return queryset
		except Role.DoesNotExist:
			return None
	def __str__(self):
		return self.name
