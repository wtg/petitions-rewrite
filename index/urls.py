from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.CreatePetitionView.as_view(), name="create"),
    path("all/", views.all, name="all"),
]
