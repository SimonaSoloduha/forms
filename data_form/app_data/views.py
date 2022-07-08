import json

from django.shortcuts import render
from django.views import generic
from django.views.generic import UpdateView

from app_data.forms import DataFormForm, InputFormForm, SelectFormForm, TextareaFormForm
from app_data.models import DataFormModel, InputForm, TextareaForm, SelectForm


class DataFormListView(generic.ListView):
    model = DataFormModel
    template_name = 'data_form_list.html'
    context_object_name = 'data_form_list'


class DataFormCreateView(UpdateView):

    def get(self, request):
        data_form = DataFormForm
        input_form = InputFormForm
        textarea_form = TextareaFormForm

        return render(
            request,
            'data_form_create.html',
            context={
                'data_form': data_form,
                'input_form': input_form,
                'textarea_form': textarea_form,
            }
        )

    def post(self, request):
        global new_data_form
        data_form = 'data_form' in request.POST and request.POST['data_form']
        if data_form:
            new_data_form = DataFormModel.objects.create(
                name=data_form
            )
        input_forms_all_new = json.loads(request.POST['input_forms_all'])
        if input_forms_all_new and new_data_form:
            for input_form in input_forms_all_new:
                InputForm.objects.create(
                    name=input_forms_all_new[input_form]['name'],
                    description=input_forms_all_new[input_form]['description'],
                    data_form=new_data_form
                )

        textarea_forms_all_new = json.loads(request.POST['textarea_forms_all'])
        if textarea_forms_all_new and new_data_form:
            for textarea_form in textarea_forms_all_new:
                TextareaForm.objects.create(
                    name=textarea_forms_all_new[textarea_form]['name'],
                    description=textarea_forms_all_new[textarea_form]['description'],
                    data_form=new_data_form
                )

        select_forms_new = json.loads(request.POST['select_forms_all'])
        if select_forms_new and new_data_form:
            for select_form in select_forms_new:
                SelectForm.objects.create(
                    name=select_forms_new[select_form]['name'],
                    description=select_forms_new[select_form]['description'],
                    choices=select_forms_new[select_form]['choices'],
                    data_form=new_data_form
                )

        return render(request, 'site_form_list_empty.html')


def update_form_view(request, data_form_id):
    if request.method == "GET":
        data_form = DataFormModel.objects.get(id=data_form_id)
        edit_data_form = DataFormForm(instance=data_form)

        input_forms = data_form.input_forms.all()
        edit_input_forms = []
        for input_form in input_forms:
            one_input_form = InputForm.objects.get(id=input_form.id)
            input_form_form = InputFormForm(instance=one_input_form)
            input_form_form.id = one_input_form.id
            edit_input_forms.append(input_form_form)

        textarea_forms = data_form.textarea_forms.all()
        edit_textarea_forms = []
        for textarea_form in textarea_forms:
            one_textarea_form = TextareaForm.objects.get(id=textarea_form.id)
            textarea_form_form = TextareaFormForm(instance=one_textarea_form)
            textarea_form_form.id = one_textarea_form.id
            edit_textarea_forms.append(textarea_form_form)

        select_forms = data_form.select_forms.all()
        edit_select_forms = []
        for select_form in select_forms:
            one_select_form = SelectForm.objects.get(id=select_form.id)
            select_form_form = SelectFormForm(instance=one_select_form)
            select_form_form.all_choices = one_select_form.choices
            select_form_form.id = one_select_form.id
            edit_select_forms.append(select_form_form)

        input_form = InputFormForm
        textarea_form = TextareaFormForm

        return render(
            request,
            'data_form_edit.html',
            context={
                'edit_data_form': edit_data_form,
                'new_data_form_id': data_form_id,
                'edit_input_forms': edit_input_forms,
                'edit_textarea_forms': edit_textarea_forms,
                'edit_select_forms': edit_select_forms,
                'input_form': input_form,
                'textarea_form': textarea_form,
            }
        )
    else:
        edit_data_form = DataFormModel.objects.get(id=data_form_id)
        input_forms_edit_list = []
        textarea_forms_edit_list = []
        select_forms_edit_list = []

        if edit_data_form.name != request.POST['data_form']:
            edit_data_form.name = request.POST['data_form']
            edit_data_form.save()

        # Редактировние

        for name in request.POST:
            if not name.find('input_forms_all_edit'):
                input_forms_edit = json.loads(request.POST['input_forms_all_edit'])
                for input_form in input_forms_edit:
                    one_input_form = InputForm.objects.get(id=int(input_form))
                    input_forms_edit_list.append(one_input_form)

                    if one_input_form.name != input_forms_edit[input_form]['value']:
                        one_input_form.name = input_forms_edit[input_form]['value']
                    if one_input_form.description != input_forms_edit[input_form]['description']:
                        one_input_form.description = input_forms_edit[input_form]['description']
                    one_input_form.save()

            if not name.find('textarea_forms_all_edit'):
                textarea_forms_edit = json.loads(request.POST['textarea_forms_all_edit'])
                for textarea_form in textarea_forms_edit:
                    one_textarea_form = TextareaForm.objects.get(id=int(textarea_form))
                    textarea_forms_edit_list.append(one_textarea_form)

                    if one_textarea_form.name != textarea_forms_edit[textarea_form]['value']:
                        one_textarea_form.name = textarea_forms_edit[textarea_form]['value']
                    if one_textarea_form.description != textarea_forms_edit[textarea_form]['description']:
                        one_textarea_form.description = textarea_forms_edit[textarea_form]['description']
                    one_textarea_form.save()

            if not name.find('select_forms_all_edit'):
                select_forms_edit = json.loads(request.POST['select_forms_all_edit'])
                for select_form in select_forms_edit:
                    one_select_form = SelectForm.objects.get(id=int(select_form))
                    select_forms_edit_list.append(one_select_form)

                    if one_select_form.name != select_forms_edit[select_form]['name']:
                        one_select_form.name = select_forms_edit[select_form]['name']
                    if one_select_form.description != select_forms_edit[select_form]['description']:
                        one_select_form.description = select_forms_edit[select_form]['description']
                    if one_select_form.choices != select_forms_edit[select_form]['choices']:
                        one_select_form.choices = select_forms_edit[select_form]['choices']
                    one_select_form.save()
        # Удаление
        inputs_to_del = list(i.id for i in edit_data_form.input_forms.all() if i not in input_forms_edit_list)
        textarea_to_del = list(i.id for i in edit_data_form.textarea_forms.all() if i not in textarea_forms_edit_list)
        select_to_del = list(i.id for i in edit_data_form.select_forms.all() if i not in select_forms_edit_list)

        for id in inputs_to_del:
            form = InputForm.objects.get(id=id)
            form.delete()
        for id in textarea_to_del:
            form = TextareaForm.objects.get(id=id)
            form.delete()
        for id in select_to_del:
            form = SelectForm.objects.get(id=id)
            form.delete()

        # Создание

        input_forms_all_new = json.loads(request.POST['input_forms_all_new'])
        for input_form in input_forms_all_new:
            InputForm.objects.create(
                name=input_forms_all_new[input_form]['name'],
                description=input_forms_all_new[input_form]['description'],
                data_form=edit_data_form
            )

        textarea_forms_all_new = json.loads(request.POST['textarea_forms_all_new'])
        for textarea_form in textarea_forms_all_new:
            TextareaForm.objects.create(
                name=textarea_forms_all_new[textarea_form]['name'],
                description=textarea_forms_all_new[textarea_form]['description'],
                data_form=edit_data_form
            )

        select_forms_new = json.loads(request.POST['select_forms_all_new'])
        for select_form in select_forms_new:
            SelectForm.objects.create(
                name=select_forms_new[select_form]['name'],
                description=select_forms_new[select_form]['description'],
                choices=select_forms_new[select_form]['choices'],
                data_form=edit_data_form
            )

        return render(request, 'site_form_list_empty.html')
