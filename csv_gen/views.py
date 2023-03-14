import os
from pathlib import Path
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import User, Schema
from django.views.generic import View

from .forms import NewSchemaForm

grac = ''


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
            global grac
            grac = 'Hello, ' + form.get('name')
            context = {
                'greetings': grac,
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
    def querydict_to_dict(query_dict):
        datas = {}
        for key in query_dict.keys():
            v = query_dict.getlist(key)
            if len(v) == 1:
                v = [v[0]]
            datas[key] = v
        return datas

    if request.method == 'POST':
        fields = ['column_name', 'type', '_from', 'to', 'order']
        data = querydict_to_dict(request.POST)

        res = ''
        for i in range(len(data['column_name'])):
            for field in fields:
                res += f'{data[field][i]}{", " if field != fields[-1] else ""}'
            res += '\n'

        new_sch = Schema()
        new_sch.name = data['name'][0]
        new_sch.modified = datetime.today().strftime('%Y-%m-%d')
        new_sch.data = res
        try:
            new_sch.save()
        except Exception as err:
            print(err)
            return HttpResponse("New Schema Name already exists in Schemas DB")

        context = {
            'header': 'FakeCSV',
            'page_name': 'Schemas',
            'head': 'New schema',
            'greetings': grac,
        }

        return render(request, 'generator.html', context)

    form = NewSchemaForm()
    context = {
        'header': 'FakeCSV',
        'page_name': 'Schemas',
        'head': 'New schema',
        'greetings': grac,
        'form': form
    }
    return render(request, 'new_schema.html', context)


def generator(request):
    file_list = {}
    if request.method == 'POST':
        d = {0: 'Name, Full name', 1: 'Mail, Email', 2: 'Bio, text'}
        for id_f in range(3):
            file_name = d[id_f].split(', ')[0] + '.csv'
            print(file_name)

            THIS_FOLDER = Path(__file__).parent.resolve()
            full_path = THIS_FOLDER / 'media' / file_name
            print(full_path)

            with open(full_path, 'w') as file:
                file_list[file.name] = (datetime.now().isoformat(), id_f + 1)
                for loops in range(int(request.POST['quant'])):
                    print(d[id_f], file=file)

    context = {
        'header': 'FakeCSV Generator.',
        'greetings': grac,
        'page_name': 'Generate cvs file',
        'head': 'Sample Schema',
        'schemas': Schema.objects.all(),
        'files': file_list
    }
    return render(request, 'generator.html', context)


def schema_view(request, schema: str):
    schema = Schema.objects.get(name=schema)
    columns = ('Column name', 'Type', 'From', 'To', 'Order',)
    rows_data = schema.data.split('\r')
    s_data = []
    for row in rows_data:
        s_data.append(dict(zip(columns, row.strip().split(', '))))
    context = {
        'schema_data': {'Name': schema.name, 'Modified': schema.modified},
        's_data': s_data,
        'header': 'Schema name: ',
        'greetings': grac,
        'page_name': schema.name.upper(),

    }
    return render(request, 'schema_view.html', context)


def schema_delete(request, schema: str):
    Schema.objects.get(name=schema).delete()
    context = {
        'greetings': grac,
        'header': 'FAKE CSV:',
        'page_name': 'Schemas',
        'schemas': Schema.objects.all(),
    }
    return render(request, 'schemas.html', context)



def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

