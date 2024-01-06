from django.http import HttpResponse
from django.shortcuts import render
from .models import place, destination


# Create your views here
def demo(request):
   obj=place.objects.all()
   objs = destination.objects.all()
   return render(request, "index.html", {'result': obj,'results':objs})

