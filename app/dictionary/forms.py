from django import forms
from django.forms import ModelForm
from .models import Word


class WordSaveUpdate(forms.ModelForm):

    word_en = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Turkish' ,
               'class':'form-control'}))
    translation_tr = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'English' ,
               'class':'form-control'}))

    class Meta:
        model = Word
        fields = ["word_en", "translation_tr"]

    