from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def thirdapp(request):
    return HttpResponse("<h1>inside third app</h1>")

