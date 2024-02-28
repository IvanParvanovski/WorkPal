from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts_app.forms.sign_up_form import SignUpForm


# Create your views here.
class SignUpCreateView(CreateView):
    form_class = SignUpForm
    template_name = 'accounts_app/sign_up.html'
    success_url = reverse_lazy('home')  # Redirect to login page upon successful form submission



