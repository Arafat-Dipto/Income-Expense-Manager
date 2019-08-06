from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.messages.views import SuccessMessageMixin




class SignUp(SuccessMessageMixin,generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    def get_success_message(self, cleaned_data):
        return "Your account has been created! You are now able to login"

