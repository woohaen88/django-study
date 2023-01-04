from django.db import models
from django.conf import settings
from django.urls import reverse


class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="article",
        null=True,
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="article/", blank=True)
    content = models.TextField(blank=True)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("articles:update", args=(self.pk,))

    def get_delete_url(self):
        return reverse("articles:delete", args=(self.pk,))

    class Meta:
        ordering = ("-updated_dt",)
