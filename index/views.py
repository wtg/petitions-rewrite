from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from .forms import CreatePetitionForm
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


def add_signature(request, pk, pk_user):

    petition = Petition.objects.get(pk=pk)

    if petition.signatures.filter(pk=pk_user).exists():
        return redirect("/petition/" + str(pk))

    user = User.objects.get(pk=pk_user)
    new_signature = Signature(signer=user)
    new_signature.save()
    petition.signatures.add(new_signature)
    petition.save()

    return redirect("/petition/" + str(pk))
