from django.db import models


# Create your models here.

class User(models.Model):
    name = models.TextField(max_length=50, unique=True)
    password = models.TextField(max_length=50)


class Schema(models.Model):
    name = models.TextField(max_length=50, unique=True)
    modified = models.DateField()
    data = models.TextField(max_length=256, null=True)

    def __str__(self):
        return f'{self.name} / {self.modified} / {self.data}'


class NewSchema(models.Model):

    TYPE_CHOICES = (
        ('Full name', 'Full Name'),
        ('Integer', 'Integer'),
        ('Company', 'Company'),
        ('Job', 'Job'),
        ('Any type', 'Any type')
    )
    column_name = models.TextField(max_length=50, unique=True)
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default='Full name',
                            )
    _from = models.IntegerField()
    to = models.IntegerField()
    order = models.IntegerField()

# class Csv_Schema(models.Model):
#     name = models.TextField(max_length=50, unique=True)
#     job = models.TextField(max_length=50)
#     email = models.EmailField()
#     Domain_name = models.TextField(max_length=50)
#     Phone_number = models.TextField(max_length=16)
#     Company_name = models.TextField(max_length=50)
