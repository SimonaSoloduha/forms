from datetime import datetime

from django.db import models
from django.urls import reverse


class DataFormModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    empty = models.BooleanField(default=0)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = 'Данные'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('data_form_list')


class InputForm(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    description = models.CharField(max_length=1500, blank=True, verbose_name='description')
    data_input = models.CharField(max_length=200, verbose_name='input')
    data_form = models.ForeignKey(DataFormModel, on_delete=models.CASCADE, related_name='input_forms')

    def __str__(self):
        return self.data_form.name


class TextareaForm(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    description = models.CharField(max_length=1500, blank=True, verbose_name='description')
    data_textarea = models.TextField(verbose_name='textarea')
    data_form = models.ForeignKey(DataFormModel, on_delete=models.CASCADE, related_name='textarea_forms')

    def __str__(self):
        return self.data_form.name


class SelectForm(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    description = models.CharField(max_length=1500, blank=True, verbose_name='description')
    choices = models.JSONField(default=dict, null=True, blank=True)
    select = models.CharField(max_length=200, verbose_name='select', blank=True)
    data_form = models.ForeignKey(DataFormModel, on_delete=models.CASCADE, related_name='select_forms')

    def __str__(self):
        return self.data_form.name
