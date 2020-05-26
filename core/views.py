from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.models import Event


# Create your views here.

# def index(req):
#   return redirect('/agenda')

def login_user(req):
  return render(req, 'login.html')

def submit_login(req):
  if req.POST:
    username = req.POST.get('username')
    password = req.POST.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
      login(req, user)
      return redirect('/')
    else:
      messages.error(req, "Username or password is invalid!")

  return redirect('/')

def logout_user(req):
  logout(req)
  return redirect('/')

@login_required(login_url='/login/')
def list_events(req):
  user = req.user
  event = Event.objects.filter(user=user)
  data = {'events': event}
  return render(req, 'agenda.html', data)

@login_required(login_url='/login/')
def event(req):
  return render(req, 'event.html')

@login_required(login_url='/login/')
def submit_event(req):
  if req.POST:
    title = req.POST.get('title')
    event_date = req.POST.get('event_date')
    desc = req.POST.get('desc')
    user = req.user
    Event.objects.create(title=title, event_date=event_date, desc=desc, user=user)
  
  return redirect('/')