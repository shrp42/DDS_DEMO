from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя Пользователя',
        'class': 'w-full py-4 px-6 rounded-xl border focus:outline-none focus:ring-2 focus:ring-teal-700 transition'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль',
        'class': 'w-full py-4 px-6 rounded-xl border focus:outline-none focus:ring-2 focus:ring-teal-700 transition'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя Пользователя',
        'class': 'w-full py-4 px-6 rounded-xl border focus:outline-none focus:ring-2 focus:ring-teal-700 transition'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите email',
        'class': 'w-full py-4 px-6 rounded-xl border focus:outline-none focus:ring-2 focus:ring-teal-700 transition'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль',
        'class': 'w-full py-4 px-6 rounded-xl border focus:outline-none focus:ring-2 focus:ring-teal-700 transition'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите пароль',
        'class': 'w-full py-4 px-6 rounded-xl border focus:outline-none focus:ring-2 focus:ring-teal-700 transition'
    }))


class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'Новый пароль (оставьте пустым, если не менять)',
            'class': 'w-full py-4 px-6 rounded-xl border focus:outline-none focus:ring-2 focus:ring-teal-700 transition'
        }),
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email')  # оставляем только username и email
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Имя пользователя',
                'class': 'w-full py-4 px-6 rounded-xl border focus:outline-none focus:ring-2 focus:ring-teal-700 transition'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'w-full py-4 px-6 rounded-xl border focus:outline-none focus:ring-2 focus:ring-teal-700 transition'
            }),
        }