# Generated by Django 2.2 on 2021-04-09 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('city', models.CharField(max_length=100, verbose_name='Город проживания')),
                ('published_news', models.IntegerField(default=0, verbose_name='Количество опубликованных новостей')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Статус верификации')),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
