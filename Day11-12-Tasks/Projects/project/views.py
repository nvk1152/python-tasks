from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    t = models.Teams(name = 'Apple Project', location = 'Banglore')
    t.save()
    d1 = models.Developers(name = 'Vamsi', skills = 'python', team = t)
    d1.save()
    d2 = models.Developers(name = 'Aishu', skills = 'java', team = t)
    d2.save()
    return HttpResponse(models.Teams.objects.filter(id=1))