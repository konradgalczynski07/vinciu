from django.shortcuts import render
from items.models import Item


def index(request):
    posted_items = Item.objects.order_by('-list_date')

    context = {
        'posted_items': posted_items
    }

    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
