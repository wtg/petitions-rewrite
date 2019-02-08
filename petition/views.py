from django.shortcuts import render, get_object_or_404
from .models import Petition

def index(request):
    return render(request, 'index.html', {'petitions': Petition.objects.all()})

def view_petition(request, petition_id):
    return render(request, 'view-petition.html', {'petition': get_object_or_404(Petition, pk=petition_id)})

def about(request):
    return render(request, 'about.html')

def create_petition(request):
    return render(request, 'create-petition.html')

def login(request):
    return render(request, 'login.html')

def view_tag(request, tag_label):
    return render(request, 'view-tag.html')