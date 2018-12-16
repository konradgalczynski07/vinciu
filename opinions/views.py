from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .choices import rating_choices
from .models import Opinion

def opinions(request, username):
    user_queryset = get_object_or_404(User, username=username)
    opinions = Opinion.objects.order_by('-list_date').filter(to_user=user_queryset)

    paginator = Paginator(opinions, 6)
    page = request.GET.get('page')
    paged_opinions = paginator.get_page(page)

    context = {
        'user_queryset': user_queryset,
        'opinions': paged_opinions
    }
    return render(request, 'opinions/opinions.html', context)


@login_required()
def new_opinion(request, username):
    user_queryset = User.objects.get(username=username)

    context = {
        'rating_choices': rating_choices,
        'user_queryset': user_queryset
    }

    if request.method == 'POST':
        from_user = request.user
        to_user = user_queryset
        rating = request.POST['rating']
        message = request.POST['message']

        opinion = Opinion(from_user=from_user, to_user=to_user,
                          rating=rating, description=message)
        try:
            opinion.save()
            messages.success(request, 'Your opinion has been submitted')
        except Exception:
            messages.error(request, 'You\'ve already given your opinion for that user')
        
        return redirect('opinions', username=username)

        
        

    else:
        return render(request, 'opinions/new-opinion.html', context)

