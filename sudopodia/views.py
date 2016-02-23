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
    return apifrom(request,eventid="0")

def apifrom(request, eventid):
    #return HttpResponse(eventid)
    eventid = int(eventid)
    i = 0
    objs = Event.objects.all()
    result = "["
    for o in objs :
        if (o.id > eventid):
            result += o.__json__()
            result += ","
    if (result[len(result)-1] != "["):
        result = result[0:len(result) - 1] + "]"
    else :
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
    name =""
    ispresent = False
    while(i < l):
        if (apikey == allu[i].apikey ):
            ispresent = True
            if (allu[i].isauth()):
	        isauth = True
                name = allu[i].Name
            else :
                isauth = False
            break
	i += 1
    if not isauth and ispresent:
        return HttpResponse("{\"Error\":\"Your api key is yet to be authorised\"}",content_type="application/json")
    if not ispresent :
        return HttpResponse("{\"Error\":\"Your api key is not found in the database. Goto the site and register one.\"}",content_type="application/json")
    newEvent = Event()
    newEvent.Name = request.POST["Name"]
    newEvent.TimeStamp = request.POST["Timestamp"]
    newEvent.Genre = request.POST["Genre"]
    newEvent.Venue = request.POST["Venue"]
    newEvent.Description = request.POST["Description"]
    newEvent.Contact = request.POST["Contact"]
    newEvent.Postscript = request.POST["Postscript"]
    newEvent.Links = request.POST["Links"]
    newEvent.PostedBy = name
    newEvent.save()
    Image = request.FILES["Image"]
    imgdata = Image.read()
    image = open("sudopodia/static/images/"+str(newEvent.id),"w")
    image.write(imgdata)
    image.close()
    return HttpResponse("{\"Message\":\"Your data has been recorded in the database}\"",content_type="application/json")
