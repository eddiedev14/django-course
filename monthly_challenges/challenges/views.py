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
    #Create base HTML dashboard structure
    response_html = f"""
        <h1>This is the challenges dashboard!</h1>
        <ul>
    """

    # Create a list based on the dictionary keys
    months = list(challenges.keys())

    # Generate dinamically the list items
    for i in range(len(months)):
        month = months[i]
        challenge_url = reverse("monthly_challenges", args=[month])
        response_html += f"<li><a href='{challenge_url}'>{month.capitalize()}</a></li>"

    # Close the ul tag
    response_html += "</ul>"

    # Returning HTML
    return HttpResponse(response_html)

# Dynamic view
def monthly_challenge(request, month):
    dashboard_path = reverse("challenges_dashboard")

    response_html = f"""<h1>The challenge is: { challenges.get(month, 'Month not found') }</h1>
                        <a href='{dashboard_path}'>Go Back</a>"""
    
    return HttpResponse(response_html)

def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("monthly_challenges", args=[redirect_month]) # Build the absolute path dinamically
    return HttpResponseRedirect(redirect_path)