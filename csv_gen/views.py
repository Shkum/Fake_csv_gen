import os
import shutil
from pathlib import Path
from datetime import datetime

from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import User, Schema
from django.views.generic import View

from .forms import NewSchemaForm

from random import choice as rnd, randrange as rnd_range

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

    form = NewSchemaForm()
    context = {
        'header': 'FakeCSV',
        'page_name': 'Schemas',
        'head': 'New schema',
        'greetings': grac,
        'form': form
    }

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
            return HttpResponse('Error: <i>' + str(err) + "</i><p>Looks like new Schema Name already exists in Schemas DB or some other error risen.</p>")

        tmp = res.strip().split('\n')
        res_dict = {}
        for i in tmp:
            res = i.strip().split(', ')
            res_dict[int(res[-1])] = res[:-1]
        res_dict = dict(sorted(res_dict.items()))
        context['res_dict'] = res_dict
        print(res_dict)
        return render(request, 'generator.html', context)

    return render(request, 'new_schema.html', context)


def clean_folder(folder):
    '''Delete all files from mentioned folder'''

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def generator(request):
    file_list = {}
    if request.method == 'POST':
        tmp = Schema.objects.all().values_list()

        tmp = list(map(lambda x: str(x).strip(), list(tmp)[-1]))
        tmp = tmp[-1].split('\n')

        res_dict = {}
        for i in tmp:
            res = i.strip().split(', ')
            res_dict[int(res[-1])] = res[:-1]
        res_dict = dict(sorted(res_dict.items()))
        # d = {0: 'Name, Full name', 1: 'Mail, Email', 2: 'Bio, text'}
        dict_data = {}
        from_to = []
        for key, val in res_dict.items():
            dict_data[key] = f'{val[0]}, {val[1]}'
            from_to.append((val[2], val[3]))

        THIS_FOLDER = Path(__file__).parent.resolve()
        clean_folder(THIS_FOLDER / 'media')

        rnd_name = ['Vasil', 'Sergiy', 'Petro', 'Ivanko', 'Dazdraperma', 'Lena']
        rnd_family = ['Shevchenko', 'Ivanenko', 'Petrenko', 'Timoshenko', 'Golovach']
        rnd_car = ['Audi', 'Toyota', 'Nissan', 'Honda', 'BMW', 'Mersedes']
        rnd_company = ['Google', 'Amazon', 'Meta', 'Yahoo']
        rnd_job = ['Programmer', 'Seamen', 'Driver', 'Manager', 'Developer']
        rnd_address = ['Kiyv', 'Odessa', 'Harkiv', 'Kherson', 'Mikolayv', 'Lviv']

        file_head = []
        file_head_type = []

        for id_f in dict_data:
            file_head.append(dict_data[id_f].strip().split(', ')[0])
            file_head_type.append(dict_data[id_f].strip().split(', ')[1])


        file_head_str = ', '.join(file_head)

        for i in range(3):
            # file_name = dict_data[id_f].split(', ')[0] + '.csv'
            file_name = f'rep0{i}' + '.csv'
            full_path = THIS_FOLDER / 'media' / file_name

            with open(full_path, 'w') as file:
                file_list[file_name] = (datetime.now().isoformat(), i + 1)

                print(file_head_str, file=file)

                for loops in range(int(request.POST['quant'])):
                    fin_name = rnd(rnd_name)
                    fin_fam = rnd(rnd_family)
                    f_name = f'{fin_fam} {fin_name}'.upper() if fin_fam == rnd_family[-1] and fin_name == rnd_name[-1] else f'{fin_fam} {fin_name}'
                    f_car = rnd(rnd_car)
                    f_company = rnd(rnd_company)
                    f_job = rnd(rnd_job)
                    f_int = 0
                    f_address = rnd(rnd_address)


                    dict_selection = {
                        'Full name': f_name,
                        'Integer': f_int,
                        'Company': f_company,
                        'Job': f_job,
                        'Car': f_car,
                        'Address': f_address,
                    }

                    final_string = []
                    for ind, typ in enumerate(file_head_type):
                        if str(file_head_type[ind]) == 'Integer':
                            dict_selection['Integer'] = rnd_range(int(from_to[ind][0]), int(from_to[ind][1]))
                        final_string.append(str(dict_selection[typ]))


                    final_string = ', '.join(final_string)
                    print(final_string, file=file)

    context = {
        'header': 'FakeCSV Generator.',
        'greetings': grac,
        'page_name': 'Generate cvs file',
        'head': 'Sample Schema',
        'schemas': Schema.objects.all(),
        'files': file_list,
        'res_dict': res_dict,
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
