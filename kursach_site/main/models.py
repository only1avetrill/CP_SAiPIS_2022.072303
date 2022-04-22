from django.db import models

# Create your models here.

class Executor(models.Model):
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
    name = models.CharField(max_length = 50, verbose_name = 'Имя')
    email = models.EmailField(null=True, verbose_name='Почта')
    address = models.CharField(max_length = 150, verbose_name = 'Адрес')
    price = models.IntegerField(verbose_name = 'Стоимость услуги')

class Ad(models.Model):
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
    title = models.CharField(max_length = 50, verbose_name = 'Название')
    area = models.IntegerField(verbose_name='Площадь заказа')
    budget = models.IntegerField(verbose_name='Бюджет')
    deadline = models.DateField(verbose_name='Срок сдачи')

    address_index = models.CharField(max_length=100, verbose_name='[Адрес] Индекс')
    address_region = models.CharField(max_length=100, verbose_name='[Адрес] Область')
    address_city = models.CharField(max_length=100, verbose_name='[Адрес] Город')
    address_street = models.CharField(max_length=100, verbose_name='[Адрес] Улица')
    address_office = models.CharField(max_length=100, verbose_name='[Адрес] Дом, корпус, помещение')

    contact = models.CharField(max_length = 300, verbose_name = 'Контактная информация')
