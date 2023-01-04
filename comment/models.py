from django.db import models

from articles.models import Article
from django.conf import settings


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.SET_NULL, null=True, related_name="comment"
    )
    writer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="comment",
    )
    content = models.TextField(blank=False)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
