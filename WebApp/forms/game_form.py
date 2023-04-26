from django import forms
from random import randint
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import IntegerField


class RandomNumberField(forms.IntegerField):
    random_number = None

    def set_random_number(self, value):
        self.random_number = value

    def validate(self, value):
        super().validate(value)
        if int(value) != self.random_number:
            raise ValidationError(self.error_messages['random_number_error'])


class GuessGameForm(forms.Form):
    def __init__(self):
        super().__init__()
        self.random_number = randint(1, 9)
        self.fields['random_number_field'].set_random_number(self.random_number)

    random_number_field = IntegerField(widget=forms.HiddenInput(), required=False)
    tries = IntegerField(initial=0, widget=forms.HiddenInput(), required=False)
    guess = RandomNumberField(
        label="Palpite",
        validators=[
            MaxValueValidator(9),
            MinValueValidator(1)
        ]
    )

    error_messages = {
        "random_number_error": "voce errou o numero",
        "max_value": "o valor maximo e 9",
        "min_value": "o valor minimo e 1",
    }


