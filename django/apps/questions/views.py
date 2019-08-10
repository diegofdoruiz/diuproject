from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from apps.questions.models import Question
from apps.questions.forms import QuestionForm
from django.urls import reverse_lazy

class QuestionList(ListView):
    model = Question
    template_name = 'question.html'

class QuestionDetail(DetailView):
    model = Question
    template_name = 'question_detail.html'

class QuestionCreate(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question_form.html'
    success_url = reverse_lazy('questions:question')

class QuestionView(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'question_form.html'
    success_url = reverse_lazy('questions:question')

class QuestionDelete(DeleteView):
    model = Question
    success_url = reverse_lazy('questions:question')