from django.forms import ModelForm
from .models import DataFormModel, InputForm, TextareaForm, SelectForm


class DataFormForm(ModelForm):
    class Meta:
        model = DataFormModel
        fields = ('name', 'empty')


class InputFormForm(ModelForm):
    class Meta:
        model = InputForm
        fields = ('name', 'description', 'data_input', 'id',)


class TextareaFormForm(ModelForm):
    class Meta:
        model = TextareaForm
        fields = ('name', 'description', 'data_textarea', 'id',)


class SelectFormForm(ModelForm):
    class Meta:
        model = SelectForm
        fields = ('name', 'description', 'choices', 'id',)
