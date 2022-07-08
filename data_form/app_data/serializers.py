from rest_framework import serializers

from app_data.models import DataFormModel, TextareaForm, SelectForm, InputForm


class InputFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = InputForm
        fields = ['id', 'name', 'data_form']


class TextareaFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextareaForm
        fields = "__all__"


class SelectFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = SelectForm
        fields = "__all__"


class DataFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataFormModel
        depth = 1
        fields = ['id', 'name', 'empty', 'input_forms', 'textarea_forms', 'select_forms']

    def create(self, validated_data):
        input_forms_data = validated_data.pop('input_forms')
        data_form = DataFormModel.objects.create(**validated_data)
        for input_data in input_forms_data:
            InputForm.objects.create(dataForm=data_form, **input_data)
        return data_form
