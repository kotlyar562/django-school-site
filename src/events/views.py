from django.core import serializers
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Event
from . forms import EventForm


def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': serializers.serialize("json", events, fields=('title', 'etype', 'date_begin', 'date_end'))})


def get_event(request):
    if request.is_ajax():
        event = get_object_or_404(Event, pk=request.GET['pk'])
        return render(request, 'events/_event.html', {'event': event})
    else:
        raise Http404


@login_required()
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Мероприятие успешно добавлено')
            return redirect('events:index')
        messages.error(request, 'Пожалуйста, исправьте ошибки.')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form':form})
