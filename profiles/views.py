from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Avg
from opinions.models import Opinion

def profile(request, username):
    user_queryset = get_object_or_404(User, username=username)
    total_comments = Opinion.objects.filter(to_user=user_queryset).count()
    avg_rating = Opinion.objects.all().filter(to_user=user_queryset).aggregate(Avg('rating'))
    

    context = {
        'user_queryset': user_queryset,
        'total_comments': total_comments,
        'avg_rating': avg_rating
    }
    return render(request, 'profiles/profile.html', context)
