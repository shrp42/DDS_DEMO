from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Category, Favorite
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer
from drf_spectacular.utils import extend_schema


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = list(request.user.favorites.values_list('item_id', flat=True))

    return render(request, "item/detail.html", {
        'item': item,
        'related_items': related_items,
        'favorite_ids': favorite_ids
    })


def category_items(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    items = Item.objects.filter(category=category, is_sold=False)

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = list(request.user.favorites.values_list('item_id', flat=True))

    return render(request, 'item/category_items.html', {
        'category': category,
        'items': items,
        'favorite_ids': favorite_ids
    })

@login_required
def toggle_favorite(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, item=item)

    if not created:
        favorite.delete()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'favorited': created})

    return redirect(request.META.get('HTTP_REFERER','/'))

@login_required
def favorites_list(request):
    favorite_items = [fav.item for fav in request.user.favorites.all()]
    return render(request, 'item/favorites.html', {
        'favorite_items': favorite_items
    })

@extend_schema(responses=ItemSerializer(many=True))
@api_view(['GET'])
def api_items_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)