from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.

class Executor(models.Model):
    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    title = models.CharField(max_length=50, verbose_name='Название')
    price = models.IntegerField(verbose_name='Стоимость услуг', validators=[MinValueValidator(0)])
    contact = models.CharField(max_length=300, verbose_name='Контактная информация')
    additionalinfo = models.CharField(max_length=500, verbose_name='Дополнительная информация')


class Ad(models.Model):
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    title = models.CharField(max_length=50, verbose_name='Название')
    area = models.IntegerField(verbose_name='Площадь заказа', validators=[MinValueValidator(0)])
    budget = models.IntegerField(verbose_name='Бюджет', validators=[MinValueValidator(0)])
    deadline = models.DateField(verbose_name='Срок сдачи')

    address_index = models.IntegerField(verbose_name='[Адрес] Индекс', validators=[MinValueValidator(0)])
    address_region = models.CharField(max_length=100, verbose_name='[Адрес] Область')
    address_city = models.CharField(max_length=100, verbose_name='[Адрес] Город')
    address_street = models.CharField(max_length=100, verbose_name='[Адрес] Улица')
    address_office = models.CharField(max_length=100, verbose_name='[Адрес] Дом, корпус, помещение')

    contact = models.CharField(max_length=300, verbose_name='Контактная информация')
