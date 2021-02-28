from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormView

from .forms import AddedCommentForm
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
	success_url = '/'


class EditNewsFormView(generic.UpdateView):
	model = NewsModel
	fields = ['title', 'content', 'is_active']
	template_name = 'news/news_updating_form.html'
	success_url = '/'


class NewsCommentFormView(generic.DetailView, FormView):
	model = NewsModel
	context_object_name = 'news'
	template_name = 'news/news_detail.html'
	form_class = AddedCommentForm

	def get_success_url(self):
		return reverse('news-detail', kwargs={'pk': self.kwargs['pk']})

	def form_valid(self, form):
		CommentModel.objects.create(news_id=self.kwargs['pk'], **form.cleaned_data)
		return super().form_valid(form)
