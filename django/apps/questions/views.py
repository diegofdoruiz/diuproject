from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from apps.questions.models import Question, Answer
from apps.questions.forms import QuestionForm, AnswerForm
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

#RESPUESTAS
class AnswerCreate(CreateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'answer_form.html'
    success_url = reverse_lazy('questions:question')

class AnswerList(ListView):
    model = Answer
    template_name = 'answer.html'

class AnswerView(UpdateView):
    model = Answer
    form_class = AnswerForm
    template_name = 'answer_form.html'
    success_url = reverse_lazy('questions:question')

class AnswerDetail(DetailView):
    model = Answer
    template_name = 'answer_detail.html'