from django.urls import path

from . import views

urlpatterns = [
    path('profile/<slug:username>/opinions/', views.opinions, name='opinions'),
    path('profile/<slug:username>/opinions/new-opinion/',
         views.new_opinion, name='new_opinion'),
]
