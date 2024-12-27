from django import forms
from django.forms import ModelForm
from .models import Word


class WordSaveUpdate(forms.ModelForm):

    word_en = forms.CharField(
        label="Turkish",
        widget=forms.TextInput(
        attrs={'placeholder': 'Turkish word...' ,
               'class':'form-control'}))
    translation_tr = forms.CharField(
        label="English",
        widget=forms.TextInput(
        attrs={'placeholder': 'English word...' ,
               'class':'form-control'}))

    class Meta:
        model = Word
        fields = ["word_en", "translation_tr"]

    