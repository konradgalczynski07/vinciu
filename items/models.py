from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

from .choices import color_choices, status_choices, category_choices

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_main = models.ImageField(upload_to='items/photos/%Y/%m/%d/')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    brand = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=status_choices)
    category = models.CharField(max_length=50, choices=category_choices)
    size = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=30)
    color = models.CharField(max_length=80, choices=color_choices, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    swap = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title
