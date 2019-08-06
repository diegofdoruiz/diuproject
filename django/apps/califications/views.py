from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from apps.califications.models import Calification
from apps.califications.forms import CalificationForm
from django.urls import reverse_lazy

class CalificationList(ListView):
    model = Calification
    template_name = 'calification.html'

class CalificationDetail(DetailView):
    model = Calification
    template_name = 'calification_detail.html'

class CalificationCreate(CreateView):
    model = Calification
    form_class = CalificationForm
    template_name = 'calification_form.html'
    success_url = reverse_lazy('califications:calification')

class CalificationView(UpdateView):
    model = Calification
    form_class = CalificationForm
    template_name = 'calification_form.html'
    success_url = reverse_lazy('califications:calification')

class CalificationDelete(DeleteView):
    model = Calification
    success_url = reverse_lazy('califications:calification')