# Generated by Django 4.1.7 on 2023-03-08 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_gen', '0007_rename_fle_name_schemas_file_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Schemas',
            new_name='Schema',
        ),
    ]
