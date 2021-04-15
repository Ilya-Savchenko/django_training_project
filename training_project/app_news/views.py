from django import forms
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView
from datetime import datetime, date

from .forms import AddedCommentForm
from .models import NewsModel



class NewsModelView(generic.ListView):
    model = NewsModel
    template_name = 'app_news/news_index.html'
    context_object_name = 'news_list'
    queryset = NewsModel.objects.filter(is_active=1).order_by('-editing_at')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        if self.request.user.has_perm('auth.can_added_news'):
            context['verified'] = True
        if self.request.user.has_perm('auth.can_publish'):
            context['moderator'] = True
        tags = set()
        for obj in NewsModel.objects.filter(is_active=1).all():
            tags.add(obj.tag)
        context['tags'] = tags
        dates = set()
        for obj in NewsModel.objects.filter(is_active=1).all():
            dates.add(obj.created_at)
        context['dates'] = dates
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=1).order_by('-editing_at')
        if 'tag' in self.request.GET:
            tag = self.request.GET['tag']
            queryset = queryset.filter(tag=tag)
        if 'date' in self.request.GET:
            dat = self.request.GET['date']
            dat = dat.split()
            year, day = int(dat[2]), int(dat[1][:-1])
            month = datetime.strptime(dat[0], '%B').month
            dat = date(year=year, month=month, day=day)
            queryset = queryset.filter(created_at=dat)
        return queryset


class CreatedNewsFormView(PermissionRequiredMixin, generic.CreateView):
    model = NewsModel
    template_name = 'app_news/news_created.html'
    fields = ['title', 'content', 'tag']
    success_url = '/'

    permission_required = 'auth.can_added_news'
    login_url = '/users/login/'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.author = self.request.user
        news.save()
        return super().form_valid(form)


class EditNewsFormView(generic.UpdateView):
    model = NewsModel
    fields = ['title', 'content', 'is_active']
    template_name = 'app_news/news_edit.html'
    success_url = '/'


class NewsCommentFormView(generic.DetailView, FormView):
    model = NewsModel
    context_object_name = 'news'
    template_name = 'app_news/news_detail.html'
    form_class = AddedCommentForm

    def get_form(self, **kwargs):
        form = super().get_form()
        if self.request.user.is_authenticated:
            form.fields['user_name'].initial = self.request.user.username
            form.fields['user_name'].widget = forms.HiddenInput()
        return form

    def get_success_url(self):
        return reverse('news-detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        comment = form.save(commit=False)
        if not self.request.user.is_authenticated:
            comment.user_name = f'{form.cleaned_data["user_name"]} (аноним)'
        else:
            comment.user_id = self.request.user.id
        comment.news_id = self.kwargs['pk']
        comment.save()
        return super().form_valid(form)

