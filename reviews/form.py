from django import forms
from .models import Review
from .widgets import starWidget
from places.models import Place

class Review_form(forms.ModelForm):
    
    place = forms.ModelChoiceField(queryset=Place.objects.all(),label="스키장")
    class Meta:
        model=Review
        exclude=("likes","user","likes_num")
        
        labels = {
            "title":"리뷰제목",
            "content":"리뷰본문",
            "rating": "별점을 남겨주세요",
        }
        widgets = {
            "rating": starWidget,
        }
        
