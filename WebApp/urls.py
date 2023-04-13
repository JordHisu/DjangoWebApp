from django.urls import path, include
from .views import game_view, home_view

game_patterns = (
    [
        path('', game_view.list, name='list'),
        path('<int:game_id>/', game_view.show, name='show'),
        # path('games/<int:game_id>/play', views.game_view),
        # path('games/<int:game_id>/scores'),
    ],
    'game'  # namespace
)


urlpatterns = [
    path(home_view.ROOT_URI, home_view.show),
    path(game_view.ROOT_URI, include(game_patterns)),
]
