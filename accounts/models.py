from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Opinion(models.Model):
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="to_user")
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="from_user")
    rating = models.IntegerField()
    description = models.TextField()
    list_date = models.DateTimeField(default=datetime.now)
