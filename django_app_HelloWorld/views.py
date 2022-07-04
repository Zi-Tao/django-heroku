from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def myIndex(request):
    return HttpResponse("Hello World!")