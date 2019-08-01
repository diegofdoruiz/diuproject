from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView,TemplateView
from apps.games.models import Game
from apps.questions.models import Question
from apps.games.forms import GameForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from diufirstprocjet.celery import app
from celery.task.control import revoke
import pyttsx3 as tts
import threading
from apps.realtime.tasks import listenArduino

@method_decorator(login_required, name='dispatch')
class GameListView(PermissionRequiredMixin, ListView):
    model = Game
    permission_required = 'games.view_game'
    template_name = 'games.html'

@method_decorator(login_required, name='dispatch')
class GameDetailView(PermissionRequiredMixin, DetailView):
    model = Game
    permission_required = 'games.view_game'
    template_name = 'game_detail.html'

@method_decorator(login_required, name='dispatch')
class GameCreateView(PermissionRequiredMixin, CreateView):
    model = Game
    permission_required = 'games.add_game'
    form_class = GameForm
    template_name = 'game_form.html'
    success_url = reverse_lazy('games:games')

@method_decorator(login_required, name='dispatch')
class GameUpdateView(PermissionRequiredMixin, UpdateView):
    model = Game
    permission_required = 'games.change_game'
    form_class = GameForm
    template_name = 'game_form.html'
    success_url = reverse_lazy('games:games')

@method_decorator(login_required, name='dispatch')
class GameDeleteView(PermissionRequiredMixin, DeleteView):
    model = Game
    permission_required = 'games.delete_game'
    success_url = reverse_lazy('games:games')

def game_start(request, pk):
    game = get_object_or_404(Game, pk=pk)
    preguntas = Question.objects.filter(game=game )
    
    
    engine = tts.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'spanish')
    engine.setProperty('rate', 140) 
    for q in preguntas : 
        engine.say(str(q.question))
        # for respuesta in list(q.answers):
        #     engine.say(str(respuesta))

    print(preguntas)
    
    print()
    engine.runAndWait()
    engine.stop()
    return render(request, 'game_start.html', {'game':game})
    

class PlayGameView(TemplateView):
    template_name = 'play_game.html'

    def get_context_data(self, **kwargs):
        context = super(PlayGameView, self).get_context_data(**kwargs)
        context['game'] = get_object_or_404(Game, pk=self.kwargs.get('pk'))
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('option') == '1':
            task_id = listenArduino.delay()
            return HttpResponse(task_id)
        elif self.request.POST.get('option') == '2':
            revoke(self.request.POST.get('task_id'), terminate=True)
            return HttpResponse('off')
        return HttpResponse('ok')
