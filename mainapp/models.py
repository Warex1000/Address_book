from django.db import models
from django.core.validators import RegexValidator


class Users(models.Model):

    name = models.CharField(max_length=20, verbose_name='Имя пользователя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия пользователя')
    country = models.CharField(max_length=30, verbose_name='Страна', blank=True)
    city = models.CharField(max_length=30, verbose_name='Город', blank=True)
    street = models.CharField(max_length=30, verbose_name='Улица', blank=True)
    url_users = models.URLField(max_length=200, verbose_name='URL пользователя', blank=True, unique=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{5,12}$',
        message="Номер телефона необходимо вводить в формате «+999999999» Допускается от 5 до 12 цифр.")
    phone = models.CharField(validators=[phone_regex], max_length=17, verbose_name='Номер телефона', blank=True)
    image = models.ImageField(verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.surname

    class Meta:
        unique_together = ('name', 'surname')
