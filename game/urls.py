from django.urls import path

from .api import GameView

app_name = 'game'

urlpatterns = [
    path('game/', GameView.as_view(), name='game_list_view'),
]