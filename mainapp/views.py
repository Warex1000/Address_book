from django.shortcuts import render, redirect

from .forms import UsersForm
from .models import Users


def index(request):
    if request.method == 'POST':
        new_user = UsersForm(request.POST, request.FILES or None)
        new_user.save()

    new_user = UsersForm()
    all_users = Users.objects.all()
    context = {'all_users': all_users, 'new_user': new_user}
    return render(request, 'mainapp/index.html', context)


def contactProfile(request, pk):
    contact = Users.objects.get(id=pk)
    all_users = Users.objects.all()
    all_users_context = {'all_users': all_users, 'info': contact}
    return render(request, 'mainapp/contact-profile.html', all_users_context)


def edit(request, pk):
    contact = Users.objects.get(id=pk)
    all_users = Users.objects.all()
    all_users_context = {'all_users': all_users, 'info': contact}
    return render(request, 'mainapp/edit-user.html', all_users_context)


# 48:40

# def delete(request, pk):
#     user = Users.objects.get(id=pk)
#     user.delete()
#
#     return redirect('/')

# def edit(request, pk):
#     user = Users.objects.get(id=pk)
#     all_users = []
#
#     for user in users:
#         users_info = dict(name=user.name, surname=user.surname, image=user.image)
#         all_users.append(users_info)
#
#     context = {'all_users': all_users}
#     return render(request, 'mainapp/edit-user.html', context)


