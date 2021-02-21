from django.contrib import admin

from .models import NewsModel, CommentModel


class CommentInLine(admin.TabularInline):
	model = CommentModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at', 'is_active']
	list_filter = ['is_active', 'created_at', 'title']
	search_fields = ['title']
	inlines = [CommentInLine]


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['user_name', 'news', 'text', 'created_at']
	list_filter = ['user_name', 'news']
	search_fields = ['user_name', 'news']
