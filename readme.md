Задание

Суть:
Реализовать адресную книгу.

Технологии:
Python- Django
Git
DRF(Опционально)

Frontend:
По JS - любой фреймворк, вплоть до чистого HTML с JQuery - лишь бы формы работали и вывод данных был понятный либо django templates.

Unit тесты, покрытие минимальное(опционально).

Данные для хранения:
Имя, фамилия (обязательные поля, уникальная комбинация)
Адрес (Страна, Город, Улица) (опциональные поля)
URL (опциональное поле, с валидацией)
Телефон
Изображение (опциональное поле, метод хранения произвольный)

Функции:
Добавление пользователя
Редактирование
Удаление
Поиск по текстовым полям

Готовое тестовое должно быть вылито на публичный гит.






My notes:

import django - install django with pycharm and test it
print(django.get_version()) - check django version
print('hello world') - test django works

django-admin startproject address_book - create new app
cd address_book - go to main folder
python manage.py startapp mainapp - create main app
register App 'mainapp' in sittings in INSTALLED_APPS
python3 manage.py makemigrations - Django использует миграции для переноса изменений в моделях (добавление поля, удаление модели и т.д.) на структуру базы данных.
python3 manage.py migrate - Start migrate
python3 manage.py migrate mainapp zero - dell all migrations
python3 manage.py migrate mainapp 0002 - dell 0002 migration
admin.site.register(Users) - register models in admin.py
python3 manage.py createsuperuser - create Super User
python3 manage.py runserver - run server 
create models in mainapp, file models.py


pip3 install pillow - install for using models.ImageField fore pictures
pip3 install requests - for requests
pip3 install -r requirements.txt - for install requests
pip freeze | xargs pip uninstall -y - for dell requests

pip3 freeze - Чтобы получить список пакетов в проекте выполняем команду
pip3 freeze > requirements.txt - Для записи вывода в requirements.txt, Команду выполняем в корне проекта. 


(example with class)
class Index(FormView):
    form_class = UsersForm
    template_name = 'mainapp/base.html'
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