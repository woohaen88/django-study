from django.db import models
from django.conf import settings
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    image = models.ImageField(upload_to="profile/", blank=True)
    nickname = models.CharField(max_length=20, unique=True, blank=True)
    message = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nickname

    def get_update_url(self):
        return reverse("profiles:update", args=(self.pk,))
