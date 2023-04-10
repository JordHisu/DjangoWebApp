from django.shortcuts import get_object_or_404, render
from django.views.generic.detail import DetailView
from ..utils import build_path

from WebApp.models import GameScore, Game


class GameShow(DetailView):
    base_path = 'game/'

    def get(self, request, game_id, **kwargs):
        game = get_object_or_404(Game, pk=game_id)
        scores = GameScore.objects.filter(game_id=game_id).order_by('-score')
        context = {'game': game, 'high_scores': scores}
        return render(request, build_path(self.base_path, 'view'), context)
