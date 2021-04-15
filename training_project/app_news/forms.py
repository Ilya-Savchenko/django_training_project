from django import forms

from .models import NewsModel, CommentModel


class CreatedNewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ['title', 'content']


class EditingNewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ['title', 'content', 'is_active']


class AddedCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['user_name', 'text']
