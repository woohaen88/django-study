from django.urls import path, re_path

from . import views

app_name = "articles"
urlpatterns = [
    path("create/", views.ArticleCreateView.as_view(), name="create"),
    re_path(
        r"^detail/(?P<pk>[-\d])/$", views.ArticleDetailView.as_view(), name="detail"
    ),
    re_path(
        r"^update/(?P<pk>[-\d])/$", views.ArticleUpdateView.as_view(), name="update"
    ),
    re_path(
        r"^delete/(?P<pk>[-\d])/$", views.ArticleDeleteView.as_view(), name="delete"
    ),
]
