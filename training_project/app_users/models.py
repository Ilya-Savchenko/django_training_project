from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    day_of_birth = models.DateField(verbose_name='День рождения')
    city = models.CharField(verbose_name='Город проживания', max_length=40, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True, unique=True)