from django.urls import path
from . import views
app_name= "reviews"

urlpatterns = [
    path("create/",views.create,name="create"),
    path("<int:review_pk>/",views.detail,name="detail"),
    path("<int:review_pk>/delete",views.delete, name="delete"),
    path("<int:review_pk>/likes",views.likes,name="likes"),
    path("<int:review_pk>/update",views.update,name="update"),
    path("",views.index,name="index"),
    path("<int:review_pk>/<int:reviewimage_pk>/image_delete/",views.image_delete,name="image_delete"),
    path("<int:review_pk>/image_add/",views.image_add,name="image_add"),
    ]
