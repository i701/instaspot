from django import forms
from .models import Drink, Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rate']
