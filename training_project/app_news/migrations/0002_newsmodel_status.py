# Generated by Django 2.2 on 2021-02-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='status',
            field=models.CharField(choices=[('a', 'Активно'), ('i', 'Неактивно')], default='a', max_length=1, verbose_name='Состояние'),
        ),
    ]