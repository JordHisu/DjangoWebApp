from django.urls import path, include
from .views import game_view, home_view, player_view

game_patterns = (
    [
        path('', game_view.list, name='list'),
        path('<int:game_id>/', game_view.show, name='show'),
        path('<int:game_id>/play', game_view.play, name='play'),
        # path('games/<int:game_id>/scores'),
    ],
    'game'  # namespace
)

player_patterns = (
    [
        path('create', player_view.CreatePlayerView.as_view(), name='create'),
    ],
    'player'  # namespace
)


urlpatterns = [
    path(home_view.ROOT_URI, home_view.show),
    path(game_view.ROOT_URI, include(game_patterns)),
    path(player_view.ROOT_URI, include(player_patterns)),
]
