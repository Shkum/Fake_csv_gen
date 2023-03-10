
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='login_page'),
    path('new_schema', new_schema, name='new_schema'),
    path('generator', generator, name='generator'),

]
