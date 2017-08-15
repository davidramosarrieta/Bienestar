from django import forms
from src.commons.models import Need

class NeedForm(forms.ModelForm):
    class Meta:
        model = Need
        fields = '__all__'
