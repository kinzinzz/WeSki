from django import forms
from django.forms import ModelForm
from .models import Review
from .widgets import starWidget
from places.models import Place

class Review_form(ModelForm):
    
    place = forms.ModelChoiceField(queryset=Place.objects.all(),label="스키장")
    
    class Meta:
        model=Review
        exclude=("likes","user","likes_num")
        
        labels = {
            "rating": "별점을 남겨주세요",
        }
        widgets = {
            "rating": starWidget,
        }
        
