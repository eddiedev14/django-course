from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return HttpResponse("This is the challenges dashboard!")

# Dynamic view
def monthly_challenge(request, month):
    challenges = {
        "1": "Walk 20 minutes every day",
        "2": "Read 10 pages of a book daily",
        "3": "Drink 2 liters of water every day",
        "4": "Learn 5 new words in another language each day",
        "5": "Wake up 30 minutes earlier than usual",
        "6": "Do 15 minutes of stretching every morning",
        "7": "Write a gratitude note daily",
        "8": "Limit social media use to 30 minutes a day",
        "9": "Eat at least one fruit and one vegetable daily",
        "10": "Practice meditation for 10 minutes every day",
        "11": "Do 20 push-ups each morning",
        "12": "Reflect and write about your year for 5 minutes daily"
    }

    return HttpResponse(f"The challenge is: { challenges.get(str(month), 'Month not found') }")