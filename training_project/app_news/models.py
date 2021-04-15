from django.conf import settings
from django.db import models


class NewsModel(models.Model):
    IS_ACTIVE_CHOICES = [('a', 'Активно'), ('i', 'Неактивно')]

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(max_length=2000, verbose_name='Текст статьи')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания', db_index=True)
    editing_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    is_active = models.BooleanField(default=False, verbose_name='Отображать в ленте')
    status = models.CharField(max_length=1, choices=IS_ACTIVE_CHOICES, verbose_name='Состояние', default='i')
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news')
    tag = models.SlugField(max_length=20, verbose_name='Тег новости')

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    user_name = models.CharField(max_length=25, verbose_name='Имя пользователя')
    text = models.TextField(max_length=1000, verbose_name='Комментарий')
    news = models.ForeignKey(to=NewsModel, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', db_index=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comments',
                             blank=True, null=True)

    def __str__(self):
        return f'{self.user_name} - {self.news}'
