from django.shortcuts import render
from django.views import generic
from .forms import CreatePetitionForm
from .models import Petition, Tag, Signature
from django.views import View
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
)


def index(request):
    petitions = Petition.objects.all().order_by("-created_date")[:6]
    context = {"petitions": petitions}
    return render(request, "index.html", context=context)


def all(request):
    return render(request, "all.html")


class CreatePetitionView(View):
    def get(self,request):
        form = CreatePetitionForm()
        tags = Tag.objects.all().order_by("-label").reverse()
        context = {
            "form": form, "tags": tags
        }

        return render(request, "create.html", context=context)
    
    def post(self,request):
        if request.method != "POST":
            return HttpResponseNotAllowed(["POST"])


        form = CreatePetitionForm(request.POST)

        if form.is_valid():

            new_petition = form.save()
            new_petition.save()
            
            ##pk = form.cleaned_data["ID"] // uncomment if you want the user to be redirected to the detail view of their petition after creation (1/2)
            
            return HttpResponseRedirect("/")
            #return HttpResponseRedirect("/petition/" + str(pk)) // uncomment if you want the user to be redirected to the detail view of their petition after creation (2/2)

        
        return HttpResponseBadRequest()
