from django.contrib.auth import login, get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from accounts.forms import (
    UserRegisterForm,
)


def register_view(request, *args, **kwargs):
    context = {}
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('article:list')
    context['form'] = form
    return render(request, 'registration/register.html', context=context)
