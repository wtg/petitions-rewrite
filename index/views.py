from django.shortcuts import render
from django.views import generic
from .forms import CreatePetitionForm
from .models import Petition, Tag


def index(request):
    petitions = Petition.objects.all().order_by("-created_date")[:6]
    context = {"petitions": petitions}
    return render(request, "index.html", context=context)


def all(request):
    return render(request, "all-petitions.html")


def create(request):
    form = CreatePetitionForm()
    context = {"form": form}
    return render(request, "create.html", context=context)

def about(request):
    return render(request, "about.html")

'''def moderation(request):
    return render(request, "about.html/#moderation")'''
