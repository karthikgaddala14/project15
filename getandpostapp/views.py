from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getinput(request):
    return render(request,'getinput.html')
def postinput(request):
    return render(request,'postinput.html')
def add(request):
    if request.method=="GET":
        x=request.GET["t1"]
        y=request.GET["t2"]
        i=int(x)
        j=int(y)
        k=i+j
        res=HttpResponse("The sum is: "+str(k))
        return res
    elif request.method=="POST":
        x=request.POST["t1"]
        y=request.POST["t2"]
        i=int(x)
        j=int(y)
        k=i+j
        res=HttpResponse("The sum is: "+str(k))
        return res
