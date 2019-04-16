# from django.forms import ModelForm
from django import forms
from .models import Petition, Tag


class CreatePetitionForm(forms.ModelForm):
    """ title = forms.CharField(max_length=200)

    description = forms.CharField(max_length=4000)  # The paragraph description """
 
    
    """
    tags = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple, queryset=Tag.objects.all(), required=True
        
    ) 
    """
    
    class Meta:
        model = Petition
        fields = ["title", "description", "tags", "ID"]
        widgets = {
            #'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : "Enter petition name here", 'aria-label' : 'Petition', 'aria-describedby' : 'add-btn'})

            #'description' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : "Enter a brief description of your petition here", 'aria-label' : 'Petition', 'aria-describedby' : 'add-btn'})


        }
    
