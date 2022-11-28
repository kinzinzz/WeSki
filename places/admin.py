from django.contrib import admin
from .models import Place


class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "address",
        "opening_time",
        "break_day",
        "contact_number",
        "price",
        "subtext",
    )


admin.site.register(Place, PlaceAdmin)
