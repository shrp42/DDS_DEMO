from unicodedata import category
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def profile(request):
    return render(request, 'core/profile.html')

def faq_view(request):
    # Список вопросов и ответов
    faq_list = [
        {"question": "Как создать аккаунт?", "answer": "Перейдите на страницу регистрации и заполните форму."},
        {"question": "Как восстановить пароль?", "answer": "На странице входа нажмите 'Забыли пароль?'."},
        {"question": "Как связаться с поддержкой?", "answer": "Используйте страницу контактов."},
        {"question": "Как купить товар?", "answer": "Для покупки или заказа товара нажмите 'Связаться с продавцом'."},
    ]
    return render(request, 'core/faq.html', {'faq_list': faq_list})

def signup(request):
        if request.method == 'POST':
            form = SignupForm(request.POST)

            if form.is_valid():
                form.save()

                return redirect('/login/')

        else:
            form = SignupForm()

        return render (request, 'core/signup.html', {
            'form': form,
        })

def logout_view(request):
    logout(request)
    return redirect('core:index')
