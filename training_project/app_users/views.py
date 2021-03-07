from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views import generic

from .forms import RegistrationForm
from .models import Profile


class LogInView(LoginView):
	template_name = 'users/login.html'



class LogOutView(LogoutView):
	next_page = '/'

def register_view(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			day_of_birth = form.cleaned_data.get('day_of_birth')
			city = form.cleaned_data.get('city')
			card_number = form.cleaned_data.get('card_number')
			phone_number = form.cleaned_data.get('phone_number')
			Profile.objects.create(
				user=user,
				city=city,
				day_of_birth=day_of_birth,
				card_number=card_number,
				phone_number=phone_number
			)
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/')
	else:
		form = RegistrationForm()
	return render(request, 'users/registration.html', {'form': form})

class AccountView(generic.ListView):
	model = User
	template_name = 'users/account.html'
	context_object_name = 'users'

