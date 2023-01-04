from django.urls import path, re_path
from . import views

app_name = "accounts"
urlpatterns = [
    path("signup/", views.AccountCreateView.as_view(), name="signup"),
    path("signin/", views.AccountLoginView.as_view(), name="signin"),
    path("signout/", views.AccountLogoutView.as_view(), name="signout"),
    re_path(
        r"^detail/(?P<pk>[-\d]+)/$", views.AccountDetailView.as_view(), name="detail"
    ),
    re_path(
        r"^update/(?P<pk>[-\d]+)/$", views.AccountUpdateView.as_view(), name="update"
    ),
    re_path(
        r"^delete/(?P<pk>[-\d]+)/$", views.AccountDeleteView.as_view(), name="delete"
    ),
]
