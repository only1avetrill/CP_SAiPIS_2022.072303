from django.forms import ModelForm, TextInput, DateInput, NumberInput, PasswordInput, TimeInput, Select, CheckboxInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class RateExecForm(UserCreationForm):
    class Meta:
        model = ExecutorRank
        fields = ['executor', 'rank']

        widgets = {
            'rank': Select(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Наименование организации (ООО, ОАО, ИП, ...)',
            })}

class AddAdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'area', 'budget', 'deadline', 'address_index', 'address_region', 'address_city',
                  'address_street', 'address_office', 'contact', 'actual', 'author']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Наименование детского сада',
            }),
            'area': NumberInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Площадь работ в кв. м.',
            }),
            'budget': NumberInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Ваш бюджет на выполнение работ в рублях',
            }),
            'deadline': DateInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Срок сдачи в формате ДД.ММ.ГГГГ',
            }),
            'address_index': NumberInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Почтовый индекс объекта работ',
            }),
            'address_region': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Область объекта работ',
            }),
            'address_city': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Населённый пункт объекта работ (г., пос., пгт., ...)',
            }),
            'address_street': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Улица объекта работ (ул., пер., пр., ...)',
            }),
            'address_office': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Номер объекта работ (зд., д., корп., ...)',
            }),
            'contact': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Контактная информация',
            }),
            'actual': CheckboxInput(
                attrs={'style': 'width:15px;height:15px'}
            ),

            'author': TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'username_author',
                'type': 'hidden',
            })
        }


class AddExecutorForm(ModelForm):
    class Meta:
        model = Executor
        fields = ['title', 'price', 'minarea', 'contact', 'additionalinfo', 'worktime_start', 'worktime_end', 'weekends', 'author']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Наименование организации (ООО, ОАО, ИП, ...)',
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Средняя стоимость работ за один кв. м. в рублях',
            }),
            'minarea': NumberInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Минимальная площадь для заказа в кв. м.',
            }),
            'contact': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Контактная информация',
            }),
            'additionalinfo': TextInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Дополнительная информация',
            }),
            'worktime_start': TimeInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Начало рабочего дня в формате ЧЧ:ММ',
            }),
            'worktime_end': TimeInput(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Окончание рабочего дня в формате ЧЧ:ММ',
            }),
            'weekends': Select(attrs={
                'class': 'form-control',
                'style': 'height: 40px',
                'placeholder': 'Выходные',
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'value': '',
                'id': 'username_author',
                'type': 'hidden',
            }),
        }
