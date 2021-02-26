from django.contrib.auth.views import LoginView, LogoutView


class LogInView(LoginView):
	template_name = 'users/login.html'


class LogOutView(LogoutView):
	next_page = '/'
