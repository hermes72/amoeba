from django.shortcuts import render
from django.http import HttpResponse
from .models import Event,User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
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

def postpage(request):
    postpager = render(request, "sudopodia/post.html")
    postpager["Access-Control-Allow-Origin"] = "*"
    return postpager

@csrf_exempt
def eventsubmit(request):
    apikey = request.POST["key"]
    allu = User.objects.all()
    l = len(allu)
    i = 0
    isauth = False
    while(i < l):
        if (apikey == allu[i].apikey and allu[i].isauth()):
	    isauth = True
	i += 1
    if not isauth :
        return HttpResponse("Your api key is not authorised or not found in the database")
    newEvent = Event()
    newEvent.Name = request.POST["Name"]
    newEvent.TimeStamp = request.POST["Timestamp"]
    newEvent.Genre = request.POST["Genre"]
    newEvent.Venue = request.POST["Venue"]
    newEvent.Description = request.POST["Description"]
    newEvent.Contact = request.POST["Contact"]
    newEvent.Postscript = request.POST["Postscript"]
    newEvent.Links = request.POST["Links"]
    newEvent.save()
    Image = request.FILES["Image"]
    imgdata = Image.read()
    image = open("sudopodia/static/images/"+str(newEvent.id),"w")
    image.write(imgdata)
    image.close()
    return HttpResponse("Your data has been recorded in the database")
