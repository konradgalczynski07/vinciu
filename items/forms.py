from django import forms

from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ( 'photo_main', 'title', 'description', 'brand', 'status', 'category', 'size', 'location', 'color', 'price', 'swap')