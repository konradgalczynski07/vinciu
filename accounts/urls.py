from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('profile/<slug:username>', views.profile, name='profile'),
    path('profile/<slug:username>/opinions', views.opinions, name='opinions'),
    path('profile/<slug:username>/opinions/new_opinion',
         views.new_opinion, name='new_opinion'),
]
