from django.shortcuts import render
from index.forms import CreatePetitionForm
from index.models import Petition

# Create your views here.

def index(request):
    return render(request, 'index.html')

def view_all(request):
    return render(request, 'all.html')

def create(request):
    form = CreatePetitionForm()
    content = {
        'form': form,
    }
    return render(request, "create.html", content)

class PetitionGridView():
    model = Petition
    context_object_name = 'petitions'
    # queryset = Petition.objects.all()