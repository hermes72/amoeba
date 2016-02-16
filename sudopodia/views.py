from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
# Create your views here.
def api(request):
    i = 0
    objs = Event.objects.all()
    l = len(objs)
    result = "["
    while (i < l) :
        result += objs[i].__json__()
	if (i != l - 1) :
	    result += ","
	i += 1
    result += "]"
    retresp = HttpResponse(result,content_type="application/json")
    return retresp

def index(request):
    return HttpResponse("wait for it")

def registerevent(request):
    return HttpResponse("Event added to the database")
