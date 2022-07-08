from django.forms import ModelForm
from django import forms


class SiteInputFormForm(ModelForm):
    data_input = forms.CharField(max_length=1000, required=True)


class SiteTextareaFormForm(ModelForm):
    data_textarea = forms.CharField(required=True)
