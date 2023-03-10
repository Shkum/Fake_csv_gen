from django.db import models

# Create your models here.

class User(models.Model):
    name = models.TextField(max_length=50, unique=True)
    password = models.TextField(max_length=50)



class Schema(models.Model):
    name = models.TextField(max_length=50, unique=True)
    modified = models.DateField()
    data = models.TextField(max_length=1024, null=True)



# class Csv_Schema(models.Model):
#     name = models.TextField(max_length=50, unique=True)
#     job = models.TextField(max_length=50)
#     email = models.EmailField()
#     Domain_name = models.TextField(max_length=50)
#     Phone_number = models.TextField(max_length=16)
#     Company_name = models.TextField(max_length=50)

