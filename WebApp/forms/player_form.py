from django.forms import ModelForm
from ..models import Player


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ["name", "nickname"]
        labels = {
            # "name": "Writer",
        }
        help_texts = {
            "name": "Informe o seu nome completo",
            "nickname": "Esta será a sua identificação única",
        }
        error_messages = {
            # "name": {
            #     "min_length": "Este nome é muito curto",
            # },
        }
