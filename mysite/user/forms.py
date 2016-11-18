from django.contrib.auth.models import User

from django.forms import ModelForm, CharField, PasswordInput, HiddenInput, Form, TextInput

BOOTSTRAP_TEXT_INPUT = TextInput(attrs={'class': 'form-control'})
BOOTSTRAP_PASS_INPUT = PasswordInput(attrs={'class': 'form-control'})


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(Form):
    next = CharField(widget=HiddenInput(), max_length=128)
    username = CharField(widget=BOOTSTRAP_TEXT_INPUT, label='Username', max_length=32, required=True)
    password = CharField(widget=BOOTSTRAP_PASS_INPUT, label='Password', max_length=32, required=True)
