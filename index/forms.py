# from django.forms import ModelForm
from django import forms
from .models import Petition, Tag


class CreatePetitionForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.all(), required=True
    )

    class Meta:
        model = Petition
        fields = ["title", "description", "tags"]
