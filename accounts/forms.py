from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

        self.fields["username"].disabled = True

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "email"]


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ["username", "email"]
