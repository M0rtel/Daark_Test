import logging

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .models import List, Folder


@login_required
def home(request):
    return render(request, 'lists/folder.html', {
        'folders': request.user.folders.all()
    })


@login_required
def folder_detail(request, folder_id):
    user_folder = get_object_or_404(Folder, id=folder_id)
    return render(request, 'lists/index.html', {
        'folder': user_folder
    })


@login_required
def list_detail(request, list_id):
    user_list = get_object_or_404(List, id=list_id)
    return render(request, 'lists/detail.html', {
        'list': user_list
    })


def login(request):
    return HttpResponse("Авторизация")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'lists/register.html'
    success_url = reverse_lazy('/login')

    # def get_queryset(self):
    #     user = self.request.user
    #     return RegisterUser.objects.filter(parent_list__user=user)

