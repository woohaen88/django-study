from articles.models import Article
from django.http import HttpResponseForbidden


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs.get("pk"))
        if not article.author == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
