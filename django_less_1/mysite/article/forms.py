from django import forms
from article.models import Article


class ArticleForm(forms.ModelForm):
    # form
    class Meta:
        model = Article
        fields = '__all__'
        labeles = {
            'title': 'Custom title',
        }
