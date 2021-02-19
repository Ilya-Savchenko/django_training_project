from django.contrib import admin

from .models import NewsModel, CommentModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
	pass

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
	pass
