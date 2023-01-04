from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    updated_dt = models.DateTimeField(auto_now=True)
    created_dt = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("accounts:detail", args=(self.id,))

    def get_update_url(self):
        return reverse("accounts:update", args=(self.id,))

    def get_delete_url(self):
        return reverse("accounts:delete", args=(self.id,))
