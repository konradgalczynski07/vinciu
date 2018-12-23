from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Item
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import ItemForm


@login_required()
def sell(request):
    if request.method == 'POST':
        item = Item(user=request.user) 
        item_form = ItemForm(request.POST, request.FILES, instance=item)
        if item_form.is_valid():
            item_form.save()
            messages.success(request, 'Item posted!')
            return redirect('profile', username=request.user.username)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        item_form = ItemForm()

    context = {
        'item_form': item_form
    }

    return render(request, 'items/sell.html', context)
    

def women(request):
    posted_items = Item.objects.all().filter(category='women')

    filtered_items = filter_items(request, posted_items)

    paginator = Paginator(filtered_items, 12)
    page = request.GET.get('page')
    paged_items = paginator.get_page(page)


    context = {
        'posted_items': paged_items
    }
    return render(request, 'items/women.html', context)


def men(request):
    posted_items = Item.objects.all().filter(category='men')

    filtered_items = filter_items(request, posted_items)

    paginator = Paginator(filtered_items, 12)
    page = request.GET.get('page')
    paged_items = paginator.get_page(page)


    context = {
        'posted_items': paged_items
    }
    return render(request, 'items/men.html', context)


def kids(request):
    posted_items = Item.objects.all().filter(category='kids')

    filtered_items = filter_items(request, posted_items)

    paginator = Paginator(filtered_items, 12)
    page = request.GET.get('page')
    paged_items = paginator.get_page(page)


    context = {
        'posted_items': paged_items
    }

    return render(request, 'items/kids.html', context)


def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item
    }

    return render(request, 'items/item.html', context)


def filter_items(request, posted_items):
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            posted_items = posted_items.filter(title__icontains=keywords)

    # Location 
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            posted_items = posted_items.filter(location__iexact=location)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            posted_items = posted_items.filter(price__lte=price)

    # Status
    if 'status' in request.GET:
        status = request.GET['status']
        if status:
            posted_items = posted_items.filter(status__iexact=status)

    return posted_items


def search(request, ):
    context = {}

    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            lookups = (Q(title__icontains=q) | 
                  Q(description__icontains=q) |
                  Q(brand__iexact=q) |
                  Q(price__icontains=q) |
                  Q(color__icontains=q) |
                  Q(location__iexact=q)
                  )
            posted_items = Item.objects.all().filter(lookups)
            context['posted_items'] = posted_items

    return render(request, 'items/search.html', context)
