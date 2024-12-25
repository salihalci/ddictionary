from django import forms
from django.forms import ModelForm
from .models import Word


class WordSaveUpdate(forms.ModelForm):

    word_en = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Turkis'}))
    translation_tr = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'English'}))

    class Meta:
        model = Word
        fields = ["word_en", "translation_tr"]
