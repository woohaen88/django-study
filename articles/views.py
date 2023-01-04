from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from articles.decorators import article_ownership_required
from articles.forms import ArticleCreationForm
from articles.models import Article
from comment.forms import CommentCreationForm

has_ownership = [
    login_required,
    article_ownership_required,
]


@method_decorator(login_required, "get")
@method_decorator(login_required, "post")
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = "articles/create.html"
    context_object_name = "article"
    success_url = reverse_lazy("articles:detail")

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.author = self.request.user
        temp_article.save()
        return super(ArticleCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("articles:detail", args=(self.object.pk,))


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = "articles/update.html"
    context_object_name = "article"
    success_url = reverse_lazy("articles:detail")

    def get_success_url(self):
        return reverse("articles:detail", args=(self.object.pk,))


class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    template_name = "articles/detail.html"
    context_object_name = "article"


@method_decorator(has_ownership, "get")
@method_decorator(has_ownership, "post")
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = "article"
    template_name = "articles/delete.html"
    success_url = reverse_lazy("index")
