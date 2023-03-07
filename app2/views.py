from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def secondapp(request):
    return HttpResponse('<h1>inside second app</h1>')
