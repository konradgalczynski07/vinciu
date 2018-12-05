from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('signup')
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email)
                    # Login after signup
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'accounts/signup.html')


@login_required(login_url="/login")
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
    else:
        return redirect('index')


def profile(request, username):
    user_queryset = get_object_or_404(User, username=username)

    context = {
        'user_queryset': user_queryset
    }
    return render(request, 'accounts/profile.html', context)


def opinions(request, username):
    user_queryset = get_object_or_404(User, username=username)

    context = {
        'user_queryset': user_queryset
    }
    return render(request, 'accounts/opinions.html', context)


def new_opinion(request, username):
    user_queryset = get_object_or_404(User, username=username)

    context = {
        'user_queryset': user_queryset
    }
    return render(request, 'accounts/new_opinion.html', context)
