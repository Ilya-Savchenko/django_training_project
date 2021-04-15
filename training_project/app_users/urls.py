from django.urls import path
from .views import (RegisterView,
                    Login,
                    Logout,
                    ProfileView,
                    ModeratorPageView,
                    ModeratorNewsListView,
                    ModeratorUnverifiedUserListView,
                    ModeratorUnverifiedUserDetailView,
                    ModeratorNewsDetailView,
                    )
urlpatterns = [
    path('registration/', RegisterView.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('moderator-page/', ModeratorPageView.as_view(), name='moderator-page'),
    path('moderator-page/news/', ModeratorNewsListView.as_view(), name='moderator-page-news'),
    path('moderator-page/news/<int:pk>/', ModeratorNewsDetailView.as_view(), name='moderator-page-news-detail'),
    path('moderator-page/users/', ModeratorUnverifiedUserListView.as_view(), name='moderator-page-users'),
    path('moderator-page/users/<int:pk>/', ModeratorUnverifiedUserDetailView.as_view(), name='moderator-page-user-detail'),
]

