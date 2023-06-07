from django.core.validators import MinLengthValidator
from django.db.models import Model, CharField


class Player(Model):
    name = CharField(max_length=50, verbose_name="Nome", validators=[MinLengthValidator(5)])
    nickname = CharField(max_length=16, verbose_name="Apelido", validators=[MinLengthValidator(5)])

