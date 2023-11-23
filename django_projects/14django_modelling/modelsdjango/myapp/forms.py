from django import forms
from .models import Article


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
