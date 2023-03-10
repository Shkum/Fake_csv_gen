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
    if request.method == 'POST':
        print('post', request.POST)
    if request.method == 'GET':
        print('get', request.GET)
    context = {
        'header': 'FakeCSV Generator.',
        'page_name': 'Generate cvs file',
        'head': 'Sample Schema',
        'schemas': Schema.objects.all(),
    }
    return render(request, 'generator.html', context)
