from django.db.models import Model
from django.db.models import TextField, CharField, TextChoices, DateTimeField


class Game(Model):
    name = CharField(max_length=30, unique=True, default="DEFAULT GAME NAME")
    rules = TextField(max_length=500, default="")
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.id})"
