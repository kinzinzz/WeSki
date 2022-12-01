from django.forms import ModelForm
from .models import Review
from .widgets import starWidget

class Review_form(ModelForm):
    class Meta:
        model=Review
        exclude=("likes","user","likes_num")
        
        labels = {
            "rating": "별점을 남겨주세요",
        }
        widgets = {
            "rating": starWidget,
        }
        
