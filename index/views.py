from django.shortcuts import render
from django.views import generic
from .forms import CreatePetitionForm
from .models import Petition, Tag
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    petitions = Petition.objects.all().order_by("-created_date")[:6]
    context = {"petitions": petitions}
    return render(request, "index.html", context=context)

#request information for the view_all petitions page
def all(request):
    #petitions2 = Petition.objects.all().order_by('archived')
    petitions = Petition.objects.all().order_by("-created_date")
    ''' paginator separates the content of page 1 with the content of page 2, so on'''
    page = request.GET.get('page', 1)
    #show 18 petitions objects per page
    paginator = Paginator(petitions, 6)
    try:
        petition_page = paginator.page(page)
    except PageNotAnInteger:
        petition_page = paginator.page(1)
    except EmptyPage:
        petition_page = paginator.page(paginator.num_pages)
    return render(request, "all-petitions.html", {'petitions': petition_page})


def create(request):
    form = CreatePetitionForm()
    context = {"form": form}
    return render(request, "create-petition.html", context=context)

def about(request):
    return render(request, "about.html")
