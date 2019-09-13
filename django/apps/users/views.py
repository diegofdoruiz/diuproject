from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView,UpdateView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from apps.users.models import User
from django.contrib.auth.models import Group
from apps.users.forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

@method_decorator(login_required, name='dispatch')
class UserListView(PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'users.view_user'
    template_name = 'users.html'

@login_required
@permission_required('users.add_user')
def create(request):
    form = UserForm(request.POST or None, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            for g in request.POST.getlist('groups'):
                group = Group.objects.get(pk=g)
                user.groups.add(group)
            return redirect('users:users')
    return render(request, 'user_form.html', {'form':form})

@login_required
@permission_required('users.change_user')
def edit(request, pk):
    instance = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=instance, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password1', '')

            if password == '':
                user.password = instance.password
            else: 
                user.set_password(password)
                print(user.username)

            user = form.save()
            user.groups.clear()
            for g in request.POST.getlist('groups'):
                group = Group.objects.get(pk=g)
                user.groups.add(group)
            return redirect('users:users')
    return render(request, 'user_form.html', {'form':form})

@method_decorator(login_required, name='dispatch')
class UserDetailView(PermissionRequiredMixin, DetailView):
    model = User
    permission_required = 'users.view_role'
    template_name = 'user_detail.html'

@method_decorator(login_required, name='dispatch')
class UserDeleteView(PermissionRequiredMixin, DeleteView):
    model = User
    permission_required = 'users.delete_user'
    success_url = reverse_lazy('users:users')

def home(request):
    if request.user.groups.filter(name = 'estudiante').exists():
        return redirect('games:play_game')
    else : 
        return redirect('home')
