from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Challenges dictionary
challenges = {
        "january": "Walk 20 minutes every day",
        "february": "Read 10 pages of a book daily",
        "march": "Drink 2 liters of water every day",
        "april": "Learn 5 new words in another language each day",
        "may": "Wake up 30 minutes earlier than usual",
        "june": "Do 15 minutes of stretching every morning",
        "july": "Write a gratitude note daily",
        "august": "Limit social media use to 30 minutes a day",
        "september": "Eat at least one fruit and one vegetable daily",
        "october": "Practice meditation for 10 minutes every day",
        "november": "Do 20 push-ups each morning",
        "december": "Reflect and write about your year for 5 minutes daily"
}

def dashboard(request):
    return HttpResponse("This is the challenges dashboard!")

# Dynamic view
def monthly_challenge(request, month):
    return HttpResponse(f"The challenge is: { challenges.get(month, 'Month not found') }")

def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenges", args=[redirect_month]) # Build the absolute path dinamically
    return HttpResponseRedirect(redirect_path)