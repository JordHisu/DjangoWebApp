from django.shortcuts import render, get_object_or_404
from ..models import Game, GameScore


ROOT_URI = 'game/'


def list(request):
    game_list = Game.objects.all().order_by('-created_at')
    context = {'game_list': game_list}
    return render(request, 'game/list.html', context)


def show(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    scores = GameScore.objects.filter(game_id=game_id).order_by('-score')
    context = {'game': game, 'high_scores': scores}
    return render(request, 'game/show.html', context)

