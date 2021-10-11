from django.shortcuts import render
from .forms import UsersForm
from .models import Users
import requests


def index(request):

    if(request.method == 'POST'):
        form = UsersForm(request.POST)
        form.save()

    form = UsersForm()
    users = Users.objects.all()
    all_users = []

    for user in users:
        users_info = {
            'name': user.name,
            'surname': user.surname,
        }
        all_users.append(users_info)

    context = {'all_users': all_users, 'form': form}
    return render(request, 'mainapp/index.html', context)
