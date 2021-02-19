from django.db import models

class NewsModel(models.Model):
	title = models.CharField(max_length=50, verbose_name='Заголовок')
	content = models.TextField(max_length=2000, verbose_name='Текст статьи')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', db_index=True)
	editing_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
	is_active = models.BooleanField(default=True, verbose_name='Отображать в ленте')

	def __str__(self):
		return self.title

class CommentModel(models.Model):
	user_name = models.CharField(max_length=25, verbose_name='Имя пользователя')
	text = models.TextField(max_length=1000, verbose_name='Комментарий')
	news = models.ForeignKey(to=NewsModel, on_delete=models.CASCADE, related_name='news')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', db_index=True)

	def __str__(self):
		return f'{self.user_name} - {self.news}'
