from django import forms
from django.contrib.auth.models import Group, Permission

class RoleForm(forms.ModelForm):
	permissions = Permission.objects.all()
	class Meta:
		model = Group
		fields = (
			'name',
			'permissions'
		)