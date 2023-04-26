from django.shortcuts import render, get_object_or_404, redirect
from ..models import Game, GameScore


ROOT_URI = 'game/'


def list(request):
    game_list = Game.objects.all().order_by('-created_at')
    context = {'game_list': game_list}
    return render(request, 'game/list.html', context)


def show(request, game_id, *redirect_content):
    game = get_object_or_404(Game, pk=game_id)
    scores = GameScore.objects.filter(game_id=game_id).order_by('-score')[:5]
    context = {'game': game, 'high_scores': scores}

    if request.method == 'POST':
        context |= {
            "result": {
                "tries": request.POST["tries"],
                "random_number": request.POST["random_number"],
                "type": request.POST["type"],
            }
        }

    return render(request, 'game/show.html', context)


def play(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    context = {'game': game}

    if request.method == 'POST':
        return redirect('game:show',
            [
                game_id,
                request.POST['type'],
                request.POST['tries'],
                request.POST['random_number'],
            ]
        )



    return render(request, 'game/play.html', context)


