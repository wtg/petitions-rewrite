from django.urls import path
import django_cas_ng.views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("all/", views.all, name="all"),
    path("petition/<int:pk>", views.petition_detail, name="petition-detail"),
    path("petition/sign", views.sign, name="sign"),
    path("login/", django_cas_ng.views.LoginView.as_view(), name="cas_ng_login"),
    path("logout/", django_cas_ng.views.LogoutView.as_view(), name="cas_ng_logout"),
]
