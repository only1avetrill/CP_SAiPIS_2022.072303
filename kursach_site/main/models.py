from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date

from requests import request


class Executor(models.Model):
    weekends = (
        ('без выходных', 'без выходных'),
        ('с выходными, требуется уточнение', 'с выходными, требуется уточнение')
    )

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    title = models.CharField(max_length=50, verbose_name='Название')
    price = models.IntegerField(verbose_name='Стоимость услуг', validators=[MinValueValidator(0)])
    minarea = models.IntegerField(verbose_name='Минимальная площадь для заказа', validators=[MinValueValidator(0)])
    contact = models.CharField(max_length=300, verbose_name='Контактная информация')
    worktime_start = models.TimeField(verbose_name='[Время работы] Начало')
    worktime_end = models.TimeField(verbose_name='[Время работы] Окончание')
    additionalinfo = models.CharField(max_length=500, verbose_name='Дополнительная информация', blank=True, null=True)
    weekends = models.CharField(max_length=50, choices=weekends)

    author = models.ForeignKey(User, on_delete=models.CASCADE)


class ExecutorRank(models.Model):
    ranks = (
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')
    )

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)
    rank = models.CharField(max_length=50, choices=ranks)


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
    actual = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
