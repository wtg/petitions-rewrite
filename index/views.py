from django.shortcuts import render
from django.views import generic
from .forms import CreatePetitionForm
from .models import Petition, Tag, Signature
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


def get_create(request):
    print("get create")
    form = CreatePetitionForm()
    tags = Tag.objects.all().order_by("-label").reverse()
    context = {
        "form": form, "tags": tags
    }

    return render(request, "create-petition.html", context=context)

def post_create(request):
    print("help")


    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])


    form = CreatePetitionForm(request.POST)
    print("created form")

    if form.is_valid():
        print("VALID FORM")
        #petition = Petition.objects.get(pk=pk)
        #description_of_petition = {etition.objects.}

        #new_petition = Petition(title=form.cleaned_data['title'],description=form.cleaned_data['description'], tags=form.cleaned_data['tags'])
        #petition.add_description(description_of_petition)

        new_petition = form.save()
    
        """ signature_of_creator = Signature(signer=request.user)
        signature_of_creator.save()
        new_petition.signatures.add(signature_of_creator) """
        new_petition.save()

        
        pk = form.cleaned_data["ID"]
        
        #return HttpResponseRedirect("/petition/" + str(pk))
        return HttpResponseRedirect("/create")

    
    return HttpResponseBadRequest()
