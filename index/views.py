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

    user_signed = False
    if petition.signatures.filter(username=request.user.username).exists():
        user_signed = True

    signatures = petition.signatures.all()
    initials = []
    for user in signatures:
        initials.append(user.first_name[0] + user.last_name[0])

    status = "Goal not met"
    if petition.check_enough_sigs():
        status = "Goal met"

    expiration_date = petition.created_date + timezone.timedelta(days=365)
    progress_percent = int((petition.signatures.count() / petition.expected_sig) * 100)
    context = {
        "petition": petition,
        "user_signed": user_signed,
        "initials": initials,
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
        petition.signatures.add(request.user)
        petition.save()
        return HttpResponseRedirect("/petition/" + str(pk))

    return HttpResponseBadRequest()
