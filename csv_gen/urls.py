import os

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='login_page'),
    path('new_schema', new_schema, name='new_schema'),
    path('generator', generator, name='generator'),
    path('schema/<str:schema>', schema_view, name='schem_view'),
    path('delete/<str:schema>', schema_delete, name='schem_delete'),
    path('download/<str:path>', download, name='download'),

]

# urlpatterns += static('/csv_gen/media/', document_root=os.path.join(settings.BASE_DIR, 'csv_gen', 'media'))
