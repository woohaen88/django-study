from django.urls import reverse
from django.views.generic import CreateView

from articles.models import Article
from comment.forms import CommentCreationForm
from comment.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = "comment/create.html"

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST["pk"])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("articles:detail", args=(self.object.article.pk,))
