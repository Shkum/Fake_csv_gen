from django.contrib import admin

from csv_gen.models import User


# admin.site.register(NewUser)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'password']

