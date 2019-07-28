from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView,UpdateView,DeleteView,DetailView
from apps.users.models import User
from django.contrib.auth.models import Group
from apps.users.forms import UserForm
from django.urls import reverse_lazy

class UserListView(ListView):
    model = User
    template_name = 'users.html'

def create(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            for g in request.POST.getlist('groups'):
                group = Group.objects.get(pk=g)
                user.groups.add(group)
            return redirect('users:users')
    return render(request, 'user_form.html', {'form':form})

def edit(request, pk):
    instance = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password1', '')
            if password == '':
                user.password = instance.password
            user = form.save()
            user.groups.clear()
            for g in request.POST.getlist('groups'):
                group = Group.objects.get(pk=g)
                user.groups.add(group)
            return redirect('users:users')
    return render(request, 'user_form.html', {'form':form})

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users:users')
