
from django import forms
from .models import Testomonial  # Spelling: Testomonial

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Enter your name", max_length=100, required=True)
    testomonial = forms.CharField(label="Enter your testomonial", max_length=1000, widget=forms.Textarea)  # Spelling: testomonial
    rating = forms.IntegerField(label="Enter your rating", max_value=5, min_value=1)
    image = forms.ImageField(label="Enter your image", required=True)

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'  # Add Bootstrap class to form fields