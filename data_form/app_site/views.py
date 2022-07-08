import re

import requests as requests
from django.shortcuts import render


def get_all_forms_empty(request):
    url = 'http://127.0.0.1:8000/data/api'
    response = requests.get(url)
    data = response.json()
    forms_id = []
    for form in data:
        if form['empty'] == 0:
            forms_id.append(str(form['id']))
    return render(request, 'site_form_list_empty.html', {'forms_id': forms_id})


def get_all_forms_not_empty(request):
    url = 'http://127.0.0.1:8000/data/api'
    response = requests.get(url)
    data = response.json()
    forms_id = []
    for form in data:
        if form['empty'] == 1:
            forms_id.append(str(form['id']))
    return render(request, 'site_form_list_not_empty.html', {'forms_id': forms_id})


def get_one_form_detail(request, pk):
    if request.method == "GET":
        url = 'http://127.0.0.1:8000/data/api/detail/' + str(pk)
        response = requests.get(url)
        data = response.json()
        input_forms = []
        textarea_forms = []
        select_forms = []

        name = data['name']
        if data['input_forms']:
            for input_form in data['input_forms']:
                input_forms.append({
                    "id": input_form['id'],
                    "name": input_form['name'],
                    "description": input_form['description'],
                    "data_input": input_form['data_input'],

                })
        if data['textarea_forms']:
            for textarea_form in data['textarea_forms']:
                textarea_forms.append({
                    "id": textarea_form['id'],
                    "name": textarea_form['name'],
                    "description": textarea_form['description'],
                    "data_textarea": textarea_form['data_textarea'],

                })
        if data['select_forms']:
            for select_form in data['select_forms']:
                select_forms.append({
                    "id": select_form['id'],
                    "name": select_form['name'],
                    "description": select_form['description'],
                    "select": select_form['select'],
                })
        return render(request, 'site_form_detail.html',
                      {'name': name,
                       'textarea_forms': textarea_forms,
                       'input_forms': input_forms,
                       'select_forms': select_forms,
                       })


def get_one_form_for_fill(request, pk):
    if request.method == "GET":
        url = 'http://127.0.0.1:8000/data/api/detail/' + str(pk)
        response = requests.get(url)
        data = response.json()
        input_forms = []
        textarea_forms = []
        select_forms = []

        name = data['name']
        if data['input_forms']:
            for input_form in data['input_forms']:
                input_forms.append({
                    "id": input_form['id'],
                    "name": input_form['name'],
                    "description": input_form['description'],
                })
        if data['textarea_forms']:
            for textarea_form in data['textarea_forms']:
                textarea_forms.append({
                    "id": textarea_form['id'],
                    "name": textarea_form['name'],
                    "description": textarea_form['description'],

                })
        if data['select_forms']:
            for select_form in data['select_forms']:
                select_forms.append({
                    "id": select_form['id'],
                    "name": select_form['name'],
                    "description": select_form['description'],
                    "choices": select_form['choices'],
                })
        return render(request, 'site_form_add_data.html',
                      {'name': name,
                       'textarea_forms': textarea_forms,
                       'input_forms': input_forms,
                       'select_forms': select_forms,
                       })
    else:
        input_forms_all = dict()
        textarea_forms_all = dict()
        select_forms_all = dict()

        for elem in request.POST:
            if not elem.find('input_forms_all'):
                id = [int(re.findall('\d+', elem)[0])][0]
                value = request.POST[f'input_forms_all[{id}]']
                input_forms_all[id] = value
            if not elem.find('textarea_forms_all'):
                id = [int(re.findall('\d+', elem)[0])][0]
                value = request.POST[f'textarea_forms_all[{id}]']
                textarea_forms_all[id] = value
            if not elem.find('select_forms_all'):
                id = [int(re.findall('\d+', elem)[0])][0]
                value = request.POST[f'select_forms_all[{id}]']
                select_forms_all[id] = value
        url = f'http://127.0.0.1:8000/data/api/detail/{str(pk)}/'
        response = requests.get(url)
        data = response.json()
        for elem in data:
            if elem == 'input_forms':
                if data[elem]:
                    for input in data[elem]:
                        input['data_input'] = input_forms_all[input['id']]
            if elem == 'select_forms':
                if data[elem]:
                    for select in data[elem]:
                        select['select'] = select_forms_all[select['id']]
            if elem == 'textarea_forms':
                if data[elem]:
                    for textarea in data[elem]:
                        textarea['data_textarea'] = textarea_forms_all[textarea['id']]
        data['empty'] = True
        res = requests.put(url, json=data)

        return render(request, 'site_form_list_empty.html')
