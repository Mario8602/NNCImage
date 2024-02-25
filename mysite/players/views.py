from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView

from .forms import (CustomUserCreationForm, UserLoginForm,
                    UpdateUserForm, UpdateProfileForm,
                    ProfileUpdateForm, ProfileCreateForm)
from .models import CustomUser, ProfileUser
from .tasks import send_subscription


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('postes')
    else:
        form = UserLoginForm()

    return render(request, 'login1.html', {"form": form})


def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    context = {
        'user': user,
    }
    return render(request, 'profile.html', context)


class ShowProfilePageView(DetailView):
    model = ProfileUser
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = ProfileUser.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(ProfileUser, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

    def post(self, request, *args, **kwargs):
        if 'subscription' in request.POST:
            send_subscription.delay()
        return redirect(to='home') # self.request.path to='home'


class CreateProfilePageView(CreateView):
    model = ProfileUser

    template_name = 'create_profile.html'
    form_class = ProfileCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profileuser)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='home')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profileuser)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})


def home_page_profile():
    pass


class ProfileUpdateView(UpdateView):

    model = ProfileUser
    template_name = 'update_profile.html'
    form_class = ProfileUpdateForm

    def get_success_url(self):
        return reverse_lazy('user_profile', kwargs={'pk': self.object.pk})
