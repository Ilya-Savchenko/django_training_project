from django.contrib import admin

from .models import VacancyModel


@admin.register(VacancyModel)
class VacancyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher']