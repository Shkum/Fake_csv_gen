from django.db import models


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
        ('Car', 'Car'),
        ('Address', 'Address')

    )
    column_name = models.TextField(max_length=50, unique=True)
    type = models.CharField(
        max_length=50,
        choices=TYPE_CHOICES,
        default='Full name',
                            )
    _from = models.IntegerField(null=True, blank=True)
    to = models.IntegerField(null=True, blank=True)
    order = models.IntegerField()
