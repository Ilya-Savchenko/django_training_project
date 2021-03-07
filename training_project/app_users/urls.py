from django.urls import path

from .views import LogInView, LogOutView, register_view, AccountView

urlpatterns = [
	path('login/', LogInView.as_view(), name='login'),
	path('logout/', LogOutView.as_view(), name='logout'),
	path('registration/', register_view, name='register'),
	path('account/', AccountView.as_view(), name='account')
]
