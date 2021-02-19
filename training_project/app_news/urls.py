from django.urls import path
from .views import NewsModelView, CreatedNewsFormView, EditNewsFormView, NewsCommentFormView



urlpatterns = [
	path('', NewsModelView.as_view(), name='news_list'),
	path('news/add_news/', CreatedNewsFormView.as_view(), name='news-add'),
	path('news/edit_news/', EditNewsFormView.as_view(), name='edit'),
	path('news/edit_news/<int:pk>/', EditNewsFormView.as_view(), name='news-update'),
	path('<int:pk>/', NewsCommentFormView.as_view(), name='news-detail')
]
