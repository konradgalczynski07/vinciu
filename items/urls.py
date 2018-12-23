from django.urls import path

from . import views

urlpatterns = [
    path('sell/', views.sell, name='sell'),
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('kids/', views.kids, name='kids'),
    path('item/<int:item_id>', views.item, name='item'), 
    path('search/', views.search, name='search'), 
]
