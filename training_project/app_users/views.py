from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.models import Group, User

from .forms import RegisterForm
from .models import UsersModel
from app_news.models import NewsModel


class RegisterView(generic.FormView):
    form_class = RegisterForm
    template_name = 'app_users/registration.html'
    success_url = '/users/profile/'

    def form_valid(self, form):
        user = form.save()
        phone_number = form.cleaned_data.get('phone_number')
        city = form.cleaned_data.get('city')
        UsersModel.objects.create(
            user=user,
            phone_number=phone_number,
            city=city,
        )
        unverified_group = Group.objects.get(name='Unverified')
        user.groups.add(unverified_group)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)

        login(self.request, user)
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'app_users/login.html'


class Logout(LogoutView):
    next_page = '/'


class ProfileView(generic.ListView):
    model = UsersModel
    template_name = 'app_users/profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        if self.request.user.has_perm('auth.can_publish'):
            context['moderator'] = True
        return context


class ModeratorPageView(PermissionRequiredMixin, View):
    permission_required = 'auth.can_publish'
    login_url = '/users/login/'

    def get(self, request):
        return render(request, template_name='app_users/moderator_page.html')


class ModeratorNewsListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'auth.can_publish'

    model = NewsModel
    context_object_name = 'news_list'
    template_name = 'app_users/moderator_news.html'
    queryset = NewsModel.objects.filter(is_active=False).order_by('-editing_at')


class ModeratorNewsDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'auth.can_publish'

    model = NewsModel
    context_object_name = 'news'
    template_name = 'app_users/moderator_news_detail.html'

    def post(self, request, *args, **kwargs):
        author_id = self.model.objects.filter(id=self.kwargs['pk'])[0].author_id
        self.model.objects.filter(id=self.kwargs['pk']).update(is_active=1)
        UsersModel.objects.filter(user_id=author_id).update(published_news=F('published_news') + 1)
        return HttpResponseRedirect('/users/moderator-page/news/')



class ModeratorUnverifiedUserListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'auth.can_verified'

    model = User
    context_object_name = 'users_list'
    template_name = 'app_users/moderator_users.html'
    queryset = UsersModel.objects.filter(is_verified=False)


class ModeratorUnverifiedUserDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'auth.can_verified'

    model = User
    template_name = 'app_users/moderator_users_profile.html'
    context_object_name = 'user_info'

    def post(self, request, *args, **kwargs):
        UsersModel.objects.filter(user_id=self.kwargs['pk']).update(is_verified=1)

        verified_group = Group.objects.get(name='Verified')
        user = self.model.objects.filter(id=self.kwargs['pk'])[0]
        user.groups.add(verified_group)

        return HttpResponseRedirect('/users/moderator-page/users/')
