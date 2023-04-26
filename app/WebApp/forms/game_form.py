from django import forms
from random import randint
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import IntegerField, CharField


class GuessGameForm(forms.Form):
    random_number = IntegerField(widget=forms.HiddenInput())
    tries = IntegerField(widget=forms.HiddenInput())
    guess = IntegerField(
        label="Seu palpite",
        validators=[
            MaxValueValidator(9),
            MinValueValidator(1)
        ],
        error_messages={
            "max_value": "o valor maximo e 9",
            "min_value": "o valor minimo e 1",
        },
        required=False
    )

    def clean(self):
        cleaned_data = super().clean()
        guess = cleaned_data.get("guess")
        random_number = cleaned_data.get("random_number")

        if "let_go" in self.data:
            return

        if guess != random_number:
            raise ValidationError("Você errou o número. Tente novamente.")




