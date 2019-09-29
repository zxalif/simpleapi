from django.urls import path

from .api import GameView

from .search import SearchGame

app_name = 'game'

# view
urlpatterns = [

]

# api
api = [
    path('api/v1/game/', GameView.as_view(), name='game_list_view'),
    path('api/v1/search/game/', SearchGame.as_view(), name='game_search_view'),
]

urlpatterns += api