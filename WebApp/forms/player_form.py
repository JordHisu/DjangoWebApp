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
            # "name": "Some useful help text.",
        }
        error_messages = {
            "name": {
                "max_length": "This name is too long.",
            },
        }
