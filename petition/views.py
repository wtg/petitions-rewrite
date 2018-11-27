from django.shortcuts import render
from petition.models import Petition

def index(request):
    return render(request, 'index.html')

def view_all(request):
    return render(request, 'view_all.html')

class PetitionGridView():
    model = Petition
    context_object_name = 'petitions'
    # queryset = Petition.objects.all()
