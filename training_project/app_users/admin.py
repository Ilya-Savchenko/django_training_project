from django.contrib import admin
from .models import UsersModel


@admin.register(UsersModel)
class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'phone_number', 'is_verified', 'published_news']
