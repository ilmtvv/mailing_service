from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.views.generic import CreateView, UpdateView, ListView
from users.models import User
from users.forms import UserForm, ProfileForm
from django.urls import reverse_lazy

from django.shortcuts import render, get_object_or_404, redirect


class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('user:profile')
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user

class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass

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
        send_mail(subject, message, from_email, recipient_list)
        return super().form_valid(form)

def confirm(request, uuid):
    user = get_object_or_404(User, uuid=uuid)
    user.is_active = True
    user.save()
    return render(request, 'users/confirm.html', {'uuid': uuid})

def succes(request):
    return render(request, 'users/succes.html')


class UserAllView(PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'mailings.manager'

@login_required
@permission_required('mailings.manager')
def checkout_status(request, pk):
    user = User.objects.get(pk=pk)

    if user.is_active == True:
        user.is_active = False
    else:
        user.is_active = True
    user.save()

    return redirect(reverse_lazy('users:all'))