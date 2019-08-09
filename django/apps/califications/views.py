from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from apps.califications.models import Calification
from apps.califications.forms import CalificationForm
from django.http import HttpResponse
from apps.questions.models import Question
from apps.games.models import Game
from apps.users.models import User

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

def sendNote(request):
    nota = request.POST.get("nota")
    question_id = request.POST.get("question")
    user = request.user
    game_id = request.POST.get("game")

    question = get_object_or_404(Question, pk=question_id)
    game = get_object_or_404(Game, pk=game_id)
    # user = get_object_or_404(User, pk=user_id)

    calification = Calification()
    calification.note = nota
    calification.question_id = question.id
    calification.student_id = user.id
    calification.game_id = game_id
    calification.save() 
    
    return HttpResponse('ok')