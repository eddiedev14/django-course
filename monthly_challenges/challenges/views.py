from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
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
        "november": None,
        "december": "Reflect and write about your year for 5 minutes daily"
}

def dashboard(request):
    # Create a list based on the dictionary keys
    months = list(challenges.keys())

    # Returning HTML
    return render(request, "challenges/dashboard.html", { "months": months })

# Dynamic view
def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]    
        return render(request, "challenges/challenge.html", { "month": month, "challenge": challenge_text })
    except:
      raise Http404()

def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())
    if month > len(months):
        raise Http404()
    
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenges", args=[redirect_month]) # Build the absolute path dinamically
    return HttpResponseRedirect(redirect_path)