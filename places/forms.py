from django import forms
from .models import Place
from django.forms import FileInput


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
            "photo_main",
            "photo_food",
            "photo_facilities",
            "photo_accommodation",
        ]
        labels = {
            "name": "상호명",
            "address": "주소",
            "opening_time": "영업 시간",
            "break_day": "휴무일",
            "contact_number": "전화번호",
            "price": "가격",
            "subtext": "설명",
            "photo_main": "메인사진",
            "photo_food": "음식사진",
            "photo_facilities": "부대시설",
            "photo_accommodation": "숙박",
        }

        widgets = {
            "photo_main": FileInput(
                attrs={
                    "id": "image_field",
                    "style": "height: 200px; width: 200px; border: 1px dashed #adb5bd; color: #adb5bd; margin-right: 10px;",
                }
            ),
            "photo_food": FileInput(
                attrs={
                    "id": "image_field",
                    "style": "height: 200px; width: 200px; border: 1px dashed #adb5bd; color: #adb5bd; margin-right: 10px;",
                }
            ),
            "photo_facilities": FileInput(
                attrs={
                    "id": "image_field",
                    "style": "height: 200px; width: 200px; border: 1px dashed #adb5bd; color: #adb5bd; margin-right: 10px;",
                }
            ),
            "photo_accommodation": FileInput(
                attrs={
                    "id": "image_field",
                    "style": "height: 200px; width: 200px; border: 1px dashed #adb5bd; color: #adb5bd; margin-right: 10px;",
                }
            ),
        }
