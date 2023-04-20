from django.http import HttpResponse
from django.shortcuts import render
from .models import Places, teams


# Create your views here.
def eyes(request):
    obj=Places.objects.all()
    obj1=teams.objects.all()
    return render(request,"index.html",{'display':obj,'details':obj1})
