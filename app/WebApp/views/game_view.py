from random import randint

from django.shortcuts import render, get_object_or_404, redirect

from ..forms.game_form import GuessGameForm
from ..models import Game, GameScore, Player

ROOT_URI = 'game/'


def list(request):
    game_list = Game.objects.all().order_by('-created_at')
    player = get_object_or_404(Player, pk=request.session['user']['id'])
    context = {'game_list': game_list, "player": player}
    return render(request, 'game/list.html', context)


def show(request, game_id, extra_context=None):
    game = get_object_or_404(Game, pk=game_id)
    player = get_object_or_404(Player, pk=request.session['user']['id'])
    scores = GameScore.objects.filter(game_id=game_id).order_by('score')[:10]
    context = {'game': game, 'player': player, 'high_scores': scores}
    if extra_context is not None:
        context |= extra_context

    return render(request, 'game/show.html', context)


def play(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    player = get_object_or_404(Player, pk=request.session['user']['id'])

    if request.method == 'GET':
        form = GuessGameForm(initial={"tries": 0, "random_number": randint(1, 9)})
    if request.method == 'POST':
        post = request.POST.copy()
        tries = int(post["tries"]) + 1
        post.update({"tries": tries})
        form = GuessGameForm(post)
        if "let_go" in post:
            context = _build_play_post_context(tries, post["random_number"], success=False)
            return show(request, game_id, extra_context=context)
        elif form.is_valid():
            context = _build_play_post_context(tries, post["random_number"], success=True)
            GameScore(player=player, game=game, score=tries).save()
            return show(request, game_id, extra_context=context)
        else:
            pass

    context = {'game': game, 'player': player, 'form': form}
    return render(request, 'game/play.html', context)


def _build_play_post_context(tries, random_number, success):
    return {
        "result": {
            "tries": tries,
            "random_number": random_number,
            "type": "SUCCESS" if success else "FAILURE"
        }
    }

