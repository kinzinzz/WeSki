from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Review, ReviewImage

class PostImageInline(admin.TabularInline):
    model = ReviewImage

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, ]

admin.site.register(Review, PostAdmin)
