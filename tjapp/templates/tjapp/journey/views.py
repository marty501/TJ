from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from tjapp.templates.tjapp.journey.forms import JourneyAddForm


def journey_default(request):
    return render(request, 'tjapp/journey/default.html')


@login_required
def journey_add(request):
    if request.method == 'POST':
        # Something
        journeyAddForm = JourneyAddForm(data=request.POST)
        if journeyAddForm.is_valid():
            # Create Journey object but don't save to the database yet
            new_journey = journeyAddForm.save(commit=False)
            new_journey.save()

    else:
        form = JourneyAddForm()
    return render(request, 'tjapp/journey/journeyadd.html', {'form': form})

