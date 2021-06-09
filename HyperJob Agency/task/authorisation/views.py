from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'authorisation/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'authorisation/login.html'
