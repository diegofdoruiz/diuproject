from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.models import Group
from apps.roles.forms import RoleForm
from django.urls import reverse_lazy

class RoleListView(ListView):
    model = Group
    template_name = 'roles.html'

class RoleDetailView(DetailView):
    model = Group
    template_name = 'role_detail.html'

class RoleCreateView(CreateView):
    model = Group
    form_class = RoleForm
    template_name = 'role_form.html'
    success_url = reverse_lazy('roles:roles')

class RoleUpdateView(UpdateView):
    model = Group
    form_class = RoleForm
    template_name = 'role_form.html'
    success_url = reverse_lazy('roles:roles')

class RoleDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('roles:roles')
