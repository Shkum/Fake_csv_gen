
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='login_page'),
    path('new_schema', new_schema, name='new_schema'),

]
