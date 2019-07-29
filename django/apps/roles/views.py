from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.models import Group
from apps.roles.forms import RoleForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

@method_decorator(login_required, name='dispatch')
class RoleListView(PermissionRequiredMixin, ListView):
    model = Group
    permission_required = 'roles.view_role'
    template_name = 'roles.html'

@method_decorator(login_required, name='dispatch')
class RoleDetailView(PermissionRequiredMixin, DetailView):
    model = Group
    permission_required = 'roles.view_role'
    template_name = 'role_detail.html'

@method_decorator(login_required, name='dispatch')
class RoleCreateView(PermissionRequiredMixin, CreateView):
    model = Group
    permission_required = 'roles.add_role'
    form_class = RoleForm
    template_name = 'role_form.html'
    success_url = reverse_lazy('roles:roles')

@method_decorator(login_required, name='dispatch')
class RoleUpdateView(PermissionRequiredMixin, UpdateView):
    model = Group
    permission_required = 'roles.change_role'
    form_class = RoleForm
    template_name = 'role_form.html'
    success_url = reverse_lazy('roles:roles')

@method_decorator(login_required, name='dispatch')
class RoleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Group
    permission_required = 'roles.delete_role'
    success_url = reverse_lazy('roles:roles')
