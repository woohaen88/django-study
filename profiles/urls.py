from django.urls import path, re_path
from . import views

app_name = "profiles"
urlpatterns = [
    path("create/", views.ProfileCreateView.as_view(), name="create"),
    re_path(
        r"^update/(?P<pk>[-\d]+)/$", views.ProfileUpdateView.as_view(), name="update"
    ),
]
