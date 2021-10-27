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


'''
(example with class)
class Index(FormView):
    form_class = UsersForm
    template_name = 'mainapp/index.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        users = Users.objects.all()
        all_users = []

        for user in users:
            users_info = {
                'name': user.name,
                'surname': user.surname,
                'image': user.image,  # add 'image': user.image,
            }
            all_users.append(users_info)

        ctx['all_users'] = all_users

        return ctx
'''


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
