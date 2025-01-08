from django import forms
from .models import *

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['rating', 'review_text']
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review here...'}),
        }
