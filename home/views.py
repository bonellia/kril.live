from django.shortcuts import render

from django.http import HttpResponse

# Create your gbapp views here.

def home(request):
    return HttpResponse("kril.live is going to host various web apps here.")

