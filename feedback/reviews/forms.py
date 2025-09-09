from django import forms

class ReviewForm(forms.Form):
    username = forms.CharField(label="Your Name", max_length=100, required=True, error_messages={
        "required": "Your name must not be empty",
        "max_length": "Please enter a short name"
    })

    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea)