from django.shortcuts import render
from django.views import generic
from .forms import CreatePetitionForm
from .models import Petition, Tag
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    petitions = Petition.objects.all().order_by("-created_date")[:6]
   # p = Paginator(petitions, 3)
    context = {"petitions": petitions}
    return render(request, "index.html", context=context)

#request information for the view_all petitions page
def all(request):
    petitions = Petition.objects.all()
    ''' paginator separates the content of page 1 with the content of page 2, so on'''
    page = request.GET.get('page', 1)
    #show 18 petitions objects per page
    paginator = Paginator(petitions, 6)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, "all-petitions.html", {'petitions': users})


def create(request):
    form = CreatePetitionForm()
    context = {"form": form}
    return render(request, "create-petition.html", context=context)

def about(request):
    return render(request, "about.html")

'''def moderation(request):
    return render(request, "about.html/#moderation")'''