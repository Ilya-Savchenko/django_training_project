from django.db import models


class VacancyModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание вакансии')
    publisher = models.CharField(max_length=30, verbose_name='Кто опубликовал')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        permissions = (
            ('can_publish', 'Может публиковать'),
        )

    def __str__(self):
        return self.title