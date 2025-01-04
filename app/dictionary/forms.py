from django import forms
from django.forms import ModelForm
from .models import Word


class WordSaveUpdate(forms.ModelForm):

    class Meta:
        model = Word
        fields = ['word_en', 'translation_tr', ]

        widgets = {


            'word_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'English...'}),
            'translation_tr': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Turkish...'}),
        }
