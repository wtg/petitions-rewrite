from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.get_create, name="create"),
    path("post-create/", views.post_create, name="post_create"),    
    path("all/", views.all, name="all"),
]
