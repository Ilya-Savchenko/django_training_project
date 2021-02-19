from django.contrib import admin

from .models import NewsModel, CommentModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at', 'is_active']

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['user_name', 'news', 'text', 'created_at']

