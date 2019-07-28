from django.urls import path
from apps.tarjetas.views import PersonajeCreateView, PersonajeUpdateView, PersonajeListView, PersonajeDeleteView, PersonajeDetailView

app_name = 'tarjetas'

urlpatterns = [
	path('', PersonajeListView.as_view(), name='personajes'),
	path('create/', PersonajeCreateView.as_view(), name='create'),
	path('<int:pk>', PersonajeDetailView.as_view(), name='detail'),
	path('edit/<int:pk>', PersonajeUpdateView.as_view(), name='edit'),
	path('delete/<int:pk>',PersonajeDeleteView.as_view(), name='delete'),
]