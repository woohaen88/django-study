from articles.models import Article


def get_articles(request):
    articles = Article.objects.all()
    return {"articles": articles}
