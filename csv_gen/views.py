from django.shortcuts import render
from .models import User, Schema
from django.views.generic import View


def index(request):
    err = None
    if request.method == 'POST':
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
            return render(request, 'Schemas.html', context)
        else:
            err = 'Incorrect login name or password'

    context = {
        'header': 'LOGING IN.',
        'page_name': 'Enter your credentials:',
        'error': err,
    }
    return render(request, 'index.html', context)


def new_schema(request):
    context = {
        'header': 'FakeCSV',
        'page_name': 'Schemas',
        'head': 'New schema'

    }
    return render(request, 'new_schema.html', context)

