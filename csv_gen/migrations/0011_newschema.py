# Generated by Django 4.1.7 on 2023-03-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_gen', '0010_schema_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.TextField(max_length=50, unique=True)),
                ('type', models.CharField(choices=[('Full name', 'Full Name'), ('Integer', 'Integer'), ('Company', 'Company'), ('Job', 'Job'), ('Any type', 'Any type')], default='Full name', max_length=50)),
                ('_from', models.IntegerField()),
                ('to', models.IntegerField()),
                ('order', models.IntegerField()),
            ],
        ),
    ]