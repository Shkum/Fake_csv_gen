import os
from pathlib import Path
from datetime import datetime

from django.shortcuts import render
from .models import User, Schema
from django.views.generic import View


class Index(View):

    def get(self, request):
        context = {
            'header': 'LOGING IN.',
            'page_name': 'Enter your credentials:',
        }
        return render(request, 'index.html', context)

    def post(self, request):

        users = dict()
        for i in User.objects.all():
            users[i.name] = i.password

        form = request.POST
        if form.get('name') in users and form.get('pass') == users[form.get('name')]:
            context = {
                'greetings': 'Hello, ' + form.get('name'),
                'header': 'FAKE CSV:',
                'page_name': 'Schemas',
                'schemas': Schema.objects.all(),
            }
            return render(request, 'schemas.html', context)
        else:
            context = {
                'error': 'Incorrect login name or password'
            }
            return render(request, 'index.html', context)


def new_schema(request):

    context = {
        'header': 'FakeCSV',
        'page_name': 'Schemas',
        'head': 'New schema'

    }
    return render(request, 'new_schema.html', context)


def generator(request):
    file_list = {}
    if request.method == 'POST':
        d = {0: 'Name, Full name', 1: 'Mail, Email', 2: 'Bio, text'}
        for id_f in range(3):
            # file_name = os.path.join('csv_gen', 'media', d[id_f].split(', ')[0] + '.csv')

            THIS_FOLDER = Path(__file__).parent.resolve()
            file_name = THIS_FOLDER / 'media' / (d[id_f].split(', ')[0] + '.csv')
            with open(file_name, 'w') as file:
                file_list[file.name] = (datetime.now().isoformat(), id_f + 1)
                for loops in range(int(request.POST['quant'])):
                    print(d[id_f], file=file)

    context = {
        'header': 'FakeCSV Generator.',
        'page_name': 'Generate cvs file',
        'head': 'Sample Schema',
        'schemas': Schema.objects.all(),
        'files': file_list
    }
    return render(request, 'generator.html', context)

