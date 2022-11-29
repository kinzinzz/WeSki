from django.forms import ModelForm
from .models import Review
class Review_form(ModelForm):
    class Meta:
        model=Review
        fields="__all__"