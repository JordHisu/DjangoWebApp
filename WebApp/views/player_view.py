from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import FormView, CreateView
from django.views.decorators.csrf import csrf_exempt
from ..forms.player_form import PlayerForm
from ..models import Player
from ..views.game_view import ROOT_URI as GAME_ROOT_URI


ROOT_URI = 'player/'


@method_decorator(csrf_exempt, name='dispatch')
class CreatePlayerView(CreateView):
    template_name = "player/create.html"
    form_class = PlayerForm
    success_url = reverse_lazy("game:list")

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session.update({"user": {"name": self.object.name, "id": self.object.id}})
        return response







