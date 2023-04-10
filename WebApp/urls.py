from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('games/', views.game_view.),
    path('games/<int:game_id>/', views.game_view),
    # path('games/<int:game_id>/play', views.game_view),
    # path('games/<int:game_id>/scores'),
]
