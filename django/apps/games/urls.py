from django.urls import path
from .views import *

app_name = 'games'

urlpatterns = [
	path('', GameListView.as_view(), name='games'),
	path('create/', GameCreateView.as_view(), name='create'),
	path('<int:pk>', GameDetailView.as_view(), name='detail'),
	path('edit/<int:pk>', GameUpdateView.as_view(), name='edit'),
	path('delete/<int:pk>', GameDeleteView.as_view(), name='delete'),
	path('play_game/<int:pk>', PlayGameView.as_view(), name='play_game'),
	path('game_start/<int:pk>', game_start, name='game_start')

]