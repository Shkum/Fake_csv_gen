import os

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='login_page'),
    path('new_schema', new_schema, name='new_schema'),
    path('generator', generator, name='generator'),

]

urlpatterns += static('/csv_gen/media/', document_root=os.path.join(settings.BASE_DIR, 'csv_gen', 'media'))

print(urlpatterns)