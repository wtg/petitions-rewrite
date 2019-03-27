from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("all/", views.all, name="all"),
    path("petition/<int:pk>", views.petition_detail, name="petition-detail"),
]
