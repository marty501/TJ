from django import forms
from django.shortcuts import render, redirect
from tjapp.models import models
from tjapp.models import Journey
from tjapp.models import User


class JourneyAddForm(forms.ModelForm):
    class Meta:
        model = Journey
        exclude = ('name', 'IsVerified', 'User')

