from django.urls import path
from .views import NewsModelView, CreatedNewsFormView, EditNewsFormView, NewsCommentFormView

urlpatterns = [
    path('', NewsModelView.as_view(), name='news_list'),
    path('news-add/', CreatedNewsFormView.as_view(), name='add_news'),
    path('news-update/<int:pk>/', EditNewsFormView.as_view(), name='news-update'),
    path('<int:pk>/', NewsCommentFormView.as_view(), name='news-detail'),
]
