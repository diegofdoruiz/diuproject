from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from apps.users.models import *


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(UserForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        # Se está actualizando el usuario, por lo tanto no es necesario el campo password de confirmación.
        # También se puede cambiar el campo password1 a texto normal, para ver qué pass se va poner
        if instance and instance.pk:
            self.fields['password1'] = forms.CharField(label='Password', required=False, widget=forms.PasswordInput)
            del self.fields['password2']
            self.fields['username'].widget.attrs['readonly'] = True

        if self.user.groups.filter(name='docente').exists():
            self.fields['groups'].queryset = Group.objects.filter(name='estudiante')

    class Meta:
        model = User
        fields = (
            'id',
        	'first_name', 
        	'last_name', 
        	'id_card', 
        	'username', 
            'groups', 
            'birthday', 
            'phone', 
            'email', 
            'address', 
            'is_active',
            'password1', 
            'password2',)