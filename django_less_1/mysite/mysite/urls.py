from django.contrib import admin
from django.urls import path

from article.views import IndexView, ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('article/create', ArticleCreateView.as_view(), name='create'),
    path('article/<int:article_id>', ArticleDetailView.as_view(), name='detail'),
    path('article/update/<int:article_id>', ArticleUpdateView.as_view(), name='update'),
    path('article/delete/<int:article_id>', ArticleDeleteView.as_view(), name='delete')
]
