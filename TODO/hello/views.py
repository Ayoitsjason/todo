from django.shortcuts import render
#import HttpResponse function from django.http
from django.http import HttpResponse

# Create your views here.
def myView(request):
    return HttpResponse("Hello there!")
