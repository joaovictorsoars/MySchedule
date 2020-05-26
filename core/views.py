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
  event_id = req.GET.get('id');
  data = {}
  if event_id:
    data['event'] = Event.objects.get(id=event_id)
  
  return render(req, 'event.html', data)

@login_required(login_url='/login/')
def submit_event(req):
  if req.POST:
    title = req.POST.get('title')
    event_date = req.POST.get('event_date')
    desc = req.POST.get('desc')
    user = req.user
    event_id = req.POST.get('event_id')

    if event_id:
      Event.objects.filter(id=event_id).update(title=title, event_date=event_date, desc=desc)
    else:
      Event.objects.create(title=title, event_date=event_date, desc=desc, user=user)
  
  return redirect('/')

@login_required(login_url='/login/')
def delete_event(req, id_event):
  user = req.user;
  event = Event.objects.get(id=id_event)
  if user == event.user:
    event.delete()

  return redirect('/')
