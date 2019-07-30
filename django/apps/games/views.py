from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from apps.games.models import Game
from apps.games.forms import GameForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

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

def play_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'play_game.html', {'game':game})

def game_start(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'game_start.html', {'game':game})
    