from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    """ Форма регистрации нового пользователя """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)
