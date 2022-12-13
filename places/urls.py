from django.urls import path, re_path
from . import views


app_name = "places"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/like/", views.like, name="like"),
    # 스키장별로 리뷰보기 url 추가(2022.12.01)
    path("<int:pk>/reviews", views.place_reviews, name="place_reviews"), 
]
