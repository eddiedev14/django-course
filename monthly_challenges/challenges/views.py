from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return HttpResponse("This is the challenges dashboard!")

def january_challenges(request):
    return HttpResponse("These are the january challenges!")

def february_challenges(request):
    return HttpResponse("These are the february challenges!")