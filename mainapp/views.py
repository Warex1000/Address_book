from django.shortcuts import render, redirect, get_object_or_404

from .forms import UsersForm
from .models import Users


def index(request):
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES or None)
        form.save()

    form = UsersForm()
    users = Users.objects.all()
    all_users = []

    for user in users:
        users_info = dict(name=user.name, surname=user.surname, image=user.image)
        all_users.append(users_info)

    context = {'all_users': all_users, 'form': form}
    return render(request, 'mainapp/index.html', context)


def delete(request, user_id):
    user = Users.objects.get(pk=user_id)
    user.delete()

    return redirect('/')


def edit(request):
    users = Users.objects.all()
    all_users = []

    for user in users:
        users_info = dict(name=user.name, surname=user.surname, image=user.image)
        all_users.append(users_info)

    context = {'all_users': all_users}
    return render(request, 'mainapp/edit.html', context)


# def edit(request, users_id):
#     users_item = get_object_or_404(Users, pk=users_id)
#     return render(request, 'mainapp/edit.html', {"users_item ": users_item })


# def edit(request, user_id):
#
#     users = Users.objects.get(pk=user_id)
#     all_users = []
#
#     for user in users:
#         users_info = dict(name=user.name, surname=user.surname, image=user.image)
#         all_users.append(users_info)
#
#     context = {'all_users': all_users, 'user': users}
#     return render(request, 'mainapp/edit.html', context)


# def edite(self, *, object_list=None, **kwargs):
#     context = super().edite(**kwargs)
#     context['users'] = Users.objects.)
#     assert isinstance(context, Users.objects)
#     return Users.objects.filter(category_id=self.kwargs['users'])






