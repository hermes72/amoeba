from django.shortcuts import render
from django.http import HttpResponse
from .models import Event,User
from django.shortcuts import render
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
    return render(request,'sudopodia/index.html')

def requestapi(request):
    name = request.POST['Name'] 
    email = request.POST['Email']
    newuser = User()
    newuser.gen(name,email)
    allu = User.objects.all()
    l = len(allu)
    i = 0
    while(i < l):
        if (email == allu[i].Email):
	    return HttpResponse("Given Email " + email + " is already registered.")
	i += 1
    newuser.save()
    return HttpResponse("Your API Key is : " + newuser.apikey + "<br>Your api key is yet to be authorised.")
