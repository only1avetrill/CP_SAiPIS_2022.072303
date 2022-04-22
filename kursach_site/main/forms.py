from django.forms import ModelForm, TextInput, DateInput, NumberInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from .models import Executor, Ad

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control mb-3',
                'style': 'height: 40px',
                'placeholder': 'Имя пользователя',
            }),
            'password1': PasswordInput(attrs={
                'class': 'form-control mb-3',
                'style': 'height: 40px',
                'placeholder': 'Пароль',
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control mb-3',
                'style': 'height: 40px',
                'placeholder': 'Повтор пароля',
            })}


class AddAdForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'area', 'budget', 'deadline', 'address_index', 'address_region', 'address_city', 'address_street', 'address_office', 'contact']

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
        }

