from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView,TemplateView
from apps.games.models import Game
from apps.topics.models import Topic
from apps.questions.models import Question
from apps.games.forms import GameForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from diufirstprocjet.celery import app
from celery.task.control import revoke, inspect
import pyttsx3 as tts
from apps.realtime.tasks import listenArduino, listenBluetooth, readText, initGame, stopGame, readTopic
from apps.califications.views import sendNote
from celery.app.task import Task
import json

from .control import test

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

class PlayGameView(TemplateView):
    # template_name = 'play_game.html'
    template_name = 'play_game2.html'
    def get_context_data(self, **kwargs):
        # test()
        context = super(PlayGameView, self).get_context_data(**kwargs)
        user= self.request.user 
        course = user.course_set.all()[0]
        game = course.game_set.all()[0]
        print(user.groups.all())
        print(course)
        print(game)
        context['game'] = game
        app.control.purge()
        return context

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('option') == '1':
            app.control.purge()
            task_id = listenArduino.delay()
            return HttpResponse(task_id)
        elif self.request.POST.get('option') == '2':
            revoke(self.request.POST.get('task_id'), terminate=True)
            return HttpResponse('off')
        return HttpResponse('ok')


class NewGameView(TemplateView):
    template_name = 'new_game.html'
    def get_context_data(self, **kwargs):
        context = super(NewGameView, self).get_context_data(**kwargs)
        context['game'] = get_object_or_404(Game, pk='1')
        app.control.purge()
        return context

    def post(self, request, *args, **kwargs):
        task_id = listenBluetooth.delay()
        return HttpResponse(task_id)
"""
def control(request):
    action = request.GET.get("action", "")
    task_id = request.GET.get("task_id", "")
    response_data = {}
    if action == "start":
        if task_id == "":
            task_id = test_button.delay()
            response_data['task'] = "running"
            response_data['task_id'] = str(task_id)
        else:
            Task.update_state(self=app, task_id=task_id, state='RUNNING')
            response_data['task'] = "re-running"
            response_data['task_id'] = str(task_id)
    elif action == "pause":
        response_data['task'] = "paused"
        response_data['task_id'] = str(task_id)
        Task.update_state(self=app, task_id=task_id, state='PAUSE')
    else:
        revoke(task_id, terminate=True)
        response_data['task'] = "terminated"
        response_data['task_id'] = ""
    return HttpResponse(json.dumps(response_data))
"""

def read_text(request):
    text = request.POST.get("text")
    key_topic = request.POST.get("key_topic")
    key_question = request.POST.get("key_question")
    to_read = request.POST.get("to_read")
    task_id = readText.delay(text=text, key_topic=key_topic, key_question=key_question, to_read=to_read)
    return HttpResponse(task_id)

"""
######################### Para el proyecto 2 #########################################
"""
def start(request):
    game_id = request.GET.get("game_id")
    # Se instancia el juego o partida
    game = get_object_or_404(Game, pk=game_id)
    if game:
        channel_game = "channelgame"+str(game.id)
        game.channel = channel_game
        game.user_id = request.user.id
        game.save()
        initGame.delay(game_id=game_id)
        response_data = {}
        response_data['task'] = "running"
        response_data['channel'] = channel_game
        return HttpResponse(json.dumps(response_data))
    return HttpResponse(json.dumps({}))

def stop(request):
    game_id = request.GET.get("game_id")
    task_id = stopGame.delay(game_id=game_id)
    response_data = {}
    response_data['task'] = "running"
    response_data['task_id'] = str(task_id)
    return HttpResponse(json.dumps(response_data))





        
