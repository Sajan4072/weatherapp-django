from django.forms import ModelForm,TextInput
from .models import Place


class PlaceForm(ModelForm):
    class Meta:
        model=Place
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'input','placeholder':'Place Name'})}