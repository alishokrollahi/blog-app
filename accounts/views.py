from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')#login & logout are predefined url patterns in django.contrib.auth.urls
    template_name = 'registration/signup.html'

