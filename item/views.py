from django.shortcuts import render

def detail(request, pk):
    item = get_objects_or_404(Item, pk=pk)