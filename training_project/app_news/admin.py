from django.contrib import admin

from .models import NewsModel, CommentModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at', 'is_active']
	list_filter = ['is_active', 'created_at', 'title']
	search_fields = ['title']

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['user_name', 'news', 'text', 'created_at']
	list_filter = ['user_name', 'news']
	search_fields = ['user_name', 'news']
