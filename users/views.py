from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from users.models import User
from users.forms import UserForm
from django.urls import reverse_lazy, reverse
from utils.email_post import email_post
class UserLoginView(LoginView):
    template_name = 'users/login.html'

class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:succes')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        subject='GO TO SITE'
        message=f'http://127.0.0.1:8000/users/register/{new_user.uuid}/'
        from_email=settings.EMAIL_HOST_USER
        recipient_list=[new_user.email]
        email_post(subject, message, from_email, recipient_list)
        return super().form_valid(form)
def confirm(request, uuid):
    user = get_object_or_404(User, uuid=uuid)
    user.is_active = True
    user.save()
    return render(request, 'users/confirm.html', {'uuid': uuid})

def succes(request):
    return render(request, 'users/succes.html')
