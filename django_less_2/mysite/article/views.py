from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Article
from .forms import ArticleForm
from account.models import Profile


class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['page_title'] = 'All titles'
        return context


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article/create.html'
    form_class = ArticleForm

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super(ArticleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article/update.html'
    form_class = ArticleForm
    pk_url_kwarg = 'article_id'

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/'
    pk_url_kwarg = 'article_id'
    template_name = 'article/confirm_delete.html'
    context_object_name = 'article'


# def index(request):
#     articles = Article.objects.all()
#     return render(request, 'index.html', {'articles': articles})

# def create(request):
#     form = ArticleForm()
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             created = form.save()

    #     created = Article.objects.create(
    #         title=request.POST.get('title'),
    #         description=request.POST.get('description')
    #     )
    #     return redirect('detail', created.id)
    # return render(request, 'article/create.html', {'form':form})


# def detail(request, article_id):
#     article = Article.objects.get(id=article_id)
#     return render(request, 'article/detail.html', {'article': article})
