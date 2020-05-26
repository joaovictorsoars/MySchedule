from django.shortcuts import render, redirect
from core.models import Event

# Create your views here.

# def index(req):
#   return redirect('/agenda')

def list_events(req):
  user = req.user
  event = Event.objects.all()
  data = {'events': event}
  return render(req, 'agenda.html', data)