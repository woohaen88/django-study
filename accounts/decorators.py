from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        User = get_user_model()
        user = User.objects.get(pk=kwargs.get("pk"))
        if user.DoesNotExist:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
