from django.shortcuts import render

from .models import *


def index(request):
    tourists = Tourist.objects.all()
    return render(request, "Tourism/index.html", {'tourists': tourists})
