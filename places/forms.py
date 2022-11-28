from django import forms
from .models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = [
            "name",
            "address",
            "opening_time",
            "break_day",
            "contact_number",
            "price",
            "subtext",
        ]
        labels = {
            "name": "상호명",
            "address": "주소",
            "opening_time": "영업 시간",
            "break_day": "휴무일",
            "contact_number": "전화번호",
            "price": "가격",
            "subtext": "설명",
        }
