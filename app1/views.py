from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstapp(request):
    return HttpResponse("<h1>inside firstapp</hi>")
