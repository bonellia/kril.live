from django.shortcuts import render

from django.http import HttpResponse

# Create your gbapp views here.

def index(request):
    return HttpResponse("goldberg machine, soon!")

