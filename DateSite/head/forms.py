from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *
from users.bulma_mixin import BulmaMixin
from django.core.validators import MinValueValidator

class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Введите имя пользоваться')
    password = forms.CharField(widget=forms.PasswordInput(),
                               label='Введите пароль')
    
    class Meta:
        model = User
        fields = ['username', 'password',]

class PhotoProfileForm(forms.ModelForm):
    image = forms.ImageField(label='Загрузите фотографию')

    class Meta:
        model = Profile
        fields = ['image',]

class AboutMeProfileForm(forms.ModelForm, BulmaMixin):
    biography = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'textarea'
    }), label='Расскажите о себе', required=False)

    class Meta:
        model = Profile
        fields = ['biography',]

class SearchForm(BulmaMixin, forms.ModelForm):
    gender = forms.ChoiceField(label='Выберите пол', choices=GENDER)
    age_min = forms.IntegerField(label='Минимальный возраст', required=False)
    age_max = forms.IntegerField(label='Максимальный возраст', required=False)
    city = forms.CharField(label='Введите город', max_length=255, required=False)

    class Meta:
        model = Profile
        fields = [
            'gender',
            'age_min',
            'age_max',
            'city',
        ]

class EditProfileForm(BulmaMixin, forms.ModelForm):
    age = forms.IntegerField(label='Ваш возраст', validators=[MinValueValidator(limit_value=18)], required=False)
    city = forms.CharField(label='Ваш город', required=False)
    job = forms.CharField(label='Ваша работа', required=False)
    hobbies = forms.CharField(label='Ваше хобби', required=False)
    status = forms.ChoiceField(label='Ваше семейное положение', choices=STATUS_CHOICE, required=False)
    gender = forms.ChoiceField(label='Выберите пол', choices=GENDER, required=False)

    class Meta:
        model = Profile
        fields = [
            'age',
            'city',
            'job',
            'hobbies',
            'status',
            'gender',
        ]

class UserForm(BulmaMixin, forms.ModelForm):
    username = forms.CharField(label='Введите имя', required=False)
    class Meta:
        model = User
        fields = ['username',]

class UploadPhotoForm(forms.ModelForm):
    photo = forms.ImageField(label='Загрузите фотографию')

    class Meta:
        model = MyPhoto
        fields = ['photo',]