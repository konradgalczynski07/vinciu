from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash, authenticate
from django.contrib.auth.models import User
from django.db.models import Avg
from opinions.models import Opinion
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm, AvatarForm


def profile(request, username):
    user_queryset = get_object_or_404(User, username=username)
    total_comments = Opinion.objects.filter(to_user=user_queryset).count()
    avg_rating = Opinion.objects.all().filter(
        to_user=user_queryset).aggregate(Avg('rating'))

    context = {
        'user_queryset': user_queryset,
        'total_comments': total_comments,
        'avg_rating': avg_rating
    }
    return render(request, 'profiles/profile.html', context)


@login_required()
def settings(request):
    if request.method == 'POST':
        avatar_form = AvatarForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if avatar_form.is_valid() and user_form.is_valid() and profile_form.is_valid():
            avatar_form.save()
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('settings')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        avatar_form = AvatarForm()
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
            'avatar_form': avatar_form,
            'user_form': user_form,
            'profile_form': profile_form
        }

    return render(request, 'profiles/settings.html', context)


@login_required()
def change_email(request):
    if request.method == 'POST':
        new_email = request.POST['new_email']
        password = request.POST['password']

        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            if User.objects.filter(email=new_email).exists():
                messages.error(request, 'That email is being used')
                return redirect('change_email')
            else:
                user.email = new_email
                user.save()
                messages.success(request, 'Your email address has been changed.')
                return redirect('settings')
        else:
            messages.error(request, 'Invalid password')
            return redirect('change_email')
            
    return render(request, 'profiles/change-email.html')

@login_required()
def change_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            user.set_password(password1)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed.')
            return redirect('settings')
        else:
            messages.error(request, 'Invalid password')
            return redirect('change_email')

    return render(request, 'profiles/change-password.html')

@login_required()
def delete_acc(request):
    if request.method == 'POST':
        password = request.POST['password']

        user = authenticate(username=request.user.username, password=password)

        if user is not None:
            user.delete()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your account has been deleted.')
            return redirect('index')
        else:
            messages.error(request, 'Invalid password')
            return redirect('delete_acc')
    return render(request, 'profiles/delete-acc.html')