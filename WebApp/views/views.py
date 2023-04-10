from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from WebApp.models import Game, GameScore


# Create your views here.
def home_page(request):
    context = {}
    return render(request, 'home.html', context)


def game_list(request):
    context = {'game_list': Game.objects.all()}
    return render(request, 'game/list.html', context)


def game_view(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    scores = GameScore.objects.filter(game_id=game_id).order_by('-score')
    context = {'game': game, 'high_scores': scores}
    return render(request, 'game/view.html', context)


