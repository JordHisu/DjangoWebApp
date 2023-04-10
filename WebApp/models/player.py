from django.db.models import Model, CharField


class Player(Model):
    name = CharField(max_length=200)

