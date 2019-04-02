from django.shortcuts import render
from django.views import generic
from django.utils import timezone
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
    signatures = petition.signatures.all()

    status = "Goal not met"
    if petition.check_enough_sigs():
        status = "Goal met"

    expiration_date = petition.created_date + timezone.timedelta(days=365)

    context = {
        "petition": petition,
        "signatures": signatures,
        "status": status,
        "date": expiration_date,
    }
    return render(request, "detail.html", context=context)


# def add_signature(request, pk, user_pk):
#     petition = Petition.objects.get(pk=pk)
#     user = User.objects.get(pk=user_pk)
#     new_signature = Signature.create(user)
#     new_signature.save()

#     petition.signatures.add(new_signature)
#     petition.save()

#     return petition_detail()
