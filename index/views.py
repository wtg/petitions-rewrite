from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    HttpResponseBadRequest,
    HttpResponseNotAllowed,
)
from .forms import CreatePetitionForm, SignPetitionForm
from .models import Petition, Tag, User, Signature


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
    signatures = petition.signatures.all()

    status = "Goal not met"
    if petition.check_enough_sigs():
        status = "Goal met"

    expiration_date = petition.created_date + timezone.timedelta(days=365)
    progress_percent = int((petition.signatures.count() / petition.expected_sig) * 100)
    context = {
        "petition": petition,
        "signatures": signatures,
        "status": status,
        "date": expiration_date,
        "progress_percent": progress_percent,
    }
    return render(request, "detail.html", context=context)


def sign(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    form = SignPetitionForm(request.POST)

    if form.is_valid():
        pk = form.cleaned_data["pk"]
        petition = Petition.objects.get(pk=pk)
        new_signature = Signature(signer=request.user)
        new_signature.save()
        petition.signatures.add(new_signature)
        petition.save()
        return HttpResponseRedirect("/petition/" + str(pk))

    return HttpResponseBadRequest()
