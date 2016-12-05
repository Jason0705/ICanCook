from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, PasswordInput, HiddenInput, Form, TextInput, EmailField, forms

BOOTSTRAP_TEXT_INPUT = TextInput(attrs={'class': 'form-control'})
BOOTSTRAP_PASS_INPUT = PasswordInput(attrs={'class': 'form-control'})


class UserForm(ModelForm):
    first_name = CharField(widget=BOOTSTRAP_TEXT_INPUT, label='First Name', required=True)
    last_name = CharField(widget=BOOTSTRAP_TEXT_INPUT, label='Last Name', required=True)
    username = CharField(widget=BOOTSTRAP_TEXT_INPUT, label='Username', max_length=32, min_length=6, required=True)
    email = EmailField(widget=BOOTSTRAP_TEXT_INPUT, label='Email', max_length=64, required=True)
    password = CharField(widget=BOOTSTRAP_PASS_INPUT, label='Password', min_length=6, max_length=32, required=True)
    password_confirm = CharField(widget=BOOTSTRAP_PASS_INPUT, label='Confirm Password', min_length=6, max_length=32, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password_confirm']

    # def clean(self):
    #     form_data = self.cleaned_data
    #
    #     password = form_data['password']
    #     password_confirm = form_data['password_confirm']
    #
    #     if password != password_confirm:
    #         del form_data["password"]
    #         del form_data["password_confirm"]
    #
    #         self.add_error("password_confirm", "Passwords do not match")
    #
    #     return form_data


class LoginForm(Form):
    next = CharField(widget=HiddenInput(), max_length=128)
    username = CharField(widget=BOOTSTRAP_TEXT_INPUT, label='Username', max_length=32, required=True)
    password = CharField(widget=BOOTSTRAP_PASS_INPUT, label='Password', max_length=32, required=True)


class UpdateUserForm(Form):
    first_name = CharField(widget=BOOTSTRAP_TEXT_INPUT, label='First Name', max_length=32, required=True)
    last_name = CharField(widget=BOOTSTRAP_TEXT_INPUT, label='Last Name', max_length=32, required=True)
    email = EmailField(widget=BOOTSTRAP_TEXT_INPUT, label='Email', max_length=64, required=True)


class UpdatePasswordForm(Form):
    current_password = CharField(widget=BOOTSTRAP_PASS_INPUT, label='Current Password', max_length=32, min_length=6,
                                 required=True)
    new_password = CharField(widget=BOOTSTRAP_PASS_INPUT, label='New Password', max_length=32, min_length=6,
                             required=True)
    new_password_confirm = CharField(widget=BOOTSTRAP_PASS_INPUT, label='Confirm New Password', min_length=6,
                                     max_length=32, required=True)
    username = ''

    def __init__(self, *args, **kwargs):
        self.username = kwargs.pop('username')
        super(UpdatePasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        form_data = self.cleaned_data

        current_password = form_data['current_password']
        user = authenticate(username=self.username, password=current_password)

        if user is None:
            del form_data["current_password"]
            del form_data["new_password"]
            del form_data["new_password_confirm"]

            self.add_error('current_password', "Current password is incorrect")
            return form_data

        new_password = form_data['new_password']
        new_password_confirm = form_data['new_password_confirm']

        if new_password != new_password_confirm:
            del form_data["current_password"]
            del form_data["new_password"]
            del form_data["new_password_confirm"]

            self.add_error("new_password_confirm", "Passwords do not match")

        return form_data
