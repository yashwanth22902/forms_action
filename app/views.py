from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
   
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,"display_topic.html",d)
    return render(request,'insert_topic.html')


def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TO=Topic.objects.get(topic_name=tn)
        NWO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)
        QLWO=Webpage.objects.all()
        d2={'topics':QLWO}
        return render(request,'display_webpage.html',d2)

    return render(request,'insert_webpage.html',d)


def select_multi(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        topiclists=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for topic_name in topiclists:
            QLWO=QLWO|Webpage.objects.filter(topic_name=topic_name)
        d1={'topics':QLWO}
        return render(request,'display_webpage.html',d1)
     

    return render(request,'select_multi.html',d)


def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'checkbox.html',d)

    
