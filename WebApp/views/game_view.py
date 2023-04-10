from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from ..models import Game, GameScore


TEMPLATE_BASE_PATH = 'game/'


def list(self, request):
    context = {'game_list': Game.objects.all()}
    return render(request, self._build_path('list'), context)

def view(self, request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    scores = GameScore.objects.filter(game_id=game_id).order_by('-score')
    context = {'game': game, 'high_scores': scores}
    return render(request, self._build_path('view'), context)

def _build_path(self, template_name: str) -> str:
    return self.template_base_path + template_name + '.html'

