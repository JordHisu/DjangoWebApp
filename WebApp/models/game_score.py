from django.db.models import Model
from django.db.models import DO_NOTHING, CASCADE
from django.db.models import ForeignKey, IntegerField, DateTimeField
from .player import Player
from .game import Game


class GameScore(Model):
    player = ForeignKey(Player, on_delete=DO_NOTHING)
    game = ForeignKey(Game, on_delete=DO_NOTHING)
    score = IntegerField(default=0)
    date = DateTimeField(auto_now_add=True)

