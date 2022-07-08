from app_data.models import DataFormModel, InputForm, TextareaForm, SelectForm
from rest_framework import permissions
from app_data.serializers import DataFormSerializer
from rest_framework import generics
from rest_framework.response import Response


class DataFormViewSet(generics.ListAPIView):
    queryset = DataFormModel.objects.all()
    serializer_class = DataFormSerializer


class DataFormViewUpdate(generics.UpdateAPIView):
    queryset = DataFormModel.objects.all()
    serializer_class = DataFormSerializer


class DataFormViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataFormModel.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DataFormSerializer

    def update(self, request, *args, **kwargs):
        data_form = self.get_object()
        data = request.data
        data_form_update = DataFormModel.objects.get(id=data['id'])
        data_form_update.empty = data['empty']
        data_form_update.save()

        data_input_forms = data['input_forms']
        data_textarea_forms = data['textarea_forms']
        data_select_forms = data['select_forms']

        for data_input_form in data_input_forms:
            input_forms = InputForm.objects.get(id=data_input_form['id'])
            input_forms.data_input = data_input_form['data_input']
            input_forms.save()

        for data_textarea_form in data_textarea_forms:
            textarea_form = TextareaForm.objects.get(id=data_textarea_form['id'])
            textarea_form.data_textarea = data_textarea_form['data_textarea']
            textarea_form.save()

        for data_input_form in data_input_forms:
            input_forms = InputForm.objects.get(id=data_input_form['id'])
            input_forms.data_input = data_input_form['data_input']
            input_forms.save()

        for data_select_form in data_select_forms:
            select_form = SelectForm.objects.get(id=data_select_form['id'])
            select_form.choices = data_select_form['choices']
            select_form.save()

        serializer = DataFormSerializer(data_form)
        return Response(serializer.data)
