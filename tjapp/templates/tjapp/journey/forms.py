from django import forms
from tjapp.models import models
from tjapp.models import Journey
from tjapp.models import Company
from tjapp.models import User
from tjapp.models import Station


class JourneyAddForm(forms.ModelForm):
    class Meta:
        model = Journey
        exclude = ('name',)
