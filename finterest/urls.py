from django.contrib import admin
from django.urls import path, include
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("profiles/", include("profiles.urls")),
    path("articles/", include("articles.urls")),
    path("comments/", include("comment.urls")),
    path("", IndexView.as_view(), name="index"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
