from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from item.models import Category, Item
from .forms import SignupForm,ProfileForm
from django.contrib import messages
from django.db.models import Q
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def index(request):
    items = Item.objects.filter(is_sold=False)[0:3]
    categories = Category.objects.all()

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = list(request.user.favorites.values_list('item_id', flat=True))

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'favorite_ids': favorite_ids
    })


def contact(request):
    return render(request, 'core/contact.html')

@login_required
def profile(request):
    return render(request, 'core/profile.html')


def faq_view(request):
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

        return render(request, 'core/signup.html', {
            'form': form,
        })


def logout_view(request):
    logout(request)
    return redirect('core:index')


def search(request):
    query = request.GET.get('query', '').strip()
    items = Item.objects.filter(is_sold=False)

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = list(request.user.favorites.values_list('item_id', flat=True))

    if query:
        items = items.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query) |
            Q(aliases__icontains=query)
        ).select_related('category').distinct()

    return render(request, 'core/search.html', {
        'items': items,
        'query': query,
        'favorite_ids': favorite_ids
    })

@login_required
def profile_edit(request):
    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        password = request.POST.get('password', '').strip()

        if form.is_valid():
            form.save()

            if password:
                user.set_password(password)
                user.save()
                messages.success(request, 'Профиль и пароль успешно обновлены!')
            else:
                messages.success(request, 'Профиль успешно обновлён!')

            return redirect('core:profile')
    else:
        form = ProfileForm(instance=user)

    return render(request, 'core/profile_edit.html', {'form': form})