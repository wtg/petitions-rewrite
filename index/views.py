from django.shortcuts import render
from django.views import generic
from .forms import CreatePetitionForm
from .models import Petition, Tag


def index(request):
    petitions = Petition.objects.all().order_by("-created_date")[:6]
    context = {"petitions": petitions}
    return render(request, "index.html", context=context)


def all(request):
    return render(request, "all.html")


def create(request):
    form = CreatePetitionForm()
    context = {"form": form}
    return render(request, "create.html", context=context)

def petition_detail(request, pk):
    petition = Petition.objects.get(pk=pk)
    context = {"petition": petition}
    return render(request, "detail.html", context=context)
