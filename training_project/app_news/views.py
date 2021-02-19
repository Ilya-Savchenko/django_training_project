from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from .forms import CreatedNewsForm, EditingNewsForm, AddedCommentForm
from .models import NewsModel, CommentModel


class NewsModelView(generic.ListView):
	model = NewsModel
	template_name = 'news/news_list.html'
	context_object_name = 'news_sort'
	queryset = NewsModel.objects.filter(is_active=1).order_by('-editing_at')


class CreatedNewsFormView(generic.CreateView):
	model = NewsModel
	template_name = 'news/news_form.html'
	fields = ['title', 'content']

	def post(self, request, *args, **kwargs):
		created_news_form = CreatedNewsForm(request.POST)
		if created_news_form.is_valid():
			NewsModel.objects.create(**created_news_form.cleaned_data)
			return HttpResponseRedirect('/')
		return render(request, 'news/created_news.html', {'created_news_form': created_news_form})


class EditNewsFormView(generic.UpdateView):
	model = NewsModel
	fields = ['title', 'content', 'is_active']
	template_name = 'news/news_updating_form.html'

	def post(self, request, *args, **kwargs):
		edit_news_form = EditingNewsForm(request.POST)
		if edit_news_form.is_valid():
			NewsModel.objects.filter(id=self.kwargs['pk']).update(editing_at=datetime.utcnow(),
			                                                   **edit_news_form.cleaned_data)
			return HttpResponseRedirect('/')
		return render(request, 'news/news_updating_form.html', context={'edit_news_form': edit_news_form})


class NewsCommentFormView(FormMixin, generic.DetailView):
	model = NewsModel
	context_object_name = 'news'
	template_name = 'news/news_detail.html'
	form_class = AddedCommentForm

	def get_success_url(self):
		return reverse('news-detail', kwargs={'pk': self.object.pk})

	def get_context_data(self, **kwargs):
		context = super(NewsCommentFormView, self).get_context_data(**kwargs)
		comments = CommentModel.objects.filter(news_id=self.kwargs['pk']).order_by('-created_at')
		context['comments'] = comments
		context['form'] = AddedCommentForm
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()

		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		CommentModel.objects.create(news_id=self.kwargs['pk'], **form.cleaned_data)
		return super().form_valid(form)
