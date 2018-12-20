from django.urls import path

from . import views

urlpatterns = [
    path('profile/<slug:username>/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('settings/email', views.change_email, name='change_email'),
    path('settings/password', views.change_password, name='change_password'),
    path('settings/delete', views.delete_acc, name='delete_acc'),
]
