from django.shortcuts import render, redirect

from .forms import UsersForm
from .models import Users


def index(request):
    if request.method == 'POST':
        new_user = UsersForm(request.POST, request.FILES or None)
        new_user.save()

    new_user = UsersForm()
    all_users = Users.objects.all()
    search_input = request.GET.get('search_area')
    if search_input:
        all_users = Users.objects.filter(surname__icontains=search_input)
    else:
        all_users = Users.objects.all()
        search_input = ''
    return render(
        request,
        'mainapp/index.html',
        {'all_users': all_users, 'new_user': new_user, 'search_input': search_input}
    )


def contactprofile(request, pk):
    contact = Users.objects.get(id=pk)
    all_users = Users.objects.all()
    all_users_context = {'all_users': all_users, 'info': contact}
    return render(request, 'mainapp/contact-profile.html', all_users_context)


def edit(request, pk):
    contact = Users.objects.get(id=pk)

    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.surname = request.POST['surname']
        contact.country = request.POST['country']
        contact.city = request.POST['city']
        contact.street = request.POST['street']
        contact.url_users = request.POST['url_users']
        contact.phone = request.POST['phone']
        contact.image = request.FILES.get('image')
        contact.save()
        return redirect('/profile/'+str(contact.id))

    all_users = Users.objects.all()
    all_users_context = {'all_users': all_users, 'info': contact}
    return render(request, 'mainapp/edit-user.html', all_users_context)


def delete(request, pk):
    user = Users.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('/')

    all_users = Users.objects.all()
    all_users_context = {'all_users': all_users, 'info': user}
    return render(request, 'mainapp/delete-user.html', all_users_context)
