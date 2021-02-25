from django.contrib import admin

from .models import NewsModel, CommentModel

class CommentInline(admin.TabularInline):
	model = CommentModel
	classes = ['collapse']

@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_at', 'editing_at','is_active', 'status']
	list_filter = ['is_active']
	inlines = [CommentInline]
	actions = ['activate', 'deactivate']

	def activate(self, request, queryset):
		queryset.update(is_active=True, status='a')
	activate.short_description = 'Отображать новость в ленте'

	def deactivate(self, request, queryset):
		queryset.update(is_active=False, status='i')
	deactivate.short_description = 'Скрыть новость из ленты'


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['user_name', 'short_comment', 'news', 'created_at']
	list_filter = ['user_name']
	actions = ['delete_comment']

	def short_comment(self, obj):
		return f'{obj.text[:15]}...' if len(obj.text) > 15 else obj.text
	short_comment.short_description = 'Текст комментария'

	def delete_comment(self, request, queryset):
		queryset.update(text='Удалено администратором')
	delete_comment.short_description = 'Удалить текст комментария'