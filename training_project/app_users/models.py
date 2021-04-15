from django.conf import settings
from django.db import models


class UsersModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='profile')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    city = models.CharField(max_length=100, verbose_name='Город проживания')
    published_news = models.IntegerField(verbose_name='Количество опубликованных новостей', default=0)
    is_verified = models.BooleanField(default=False, verbose_name='Статус верификации')

