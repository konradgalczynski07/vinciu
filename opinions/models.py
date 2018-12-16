from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from .choices import rating_choices


class Opinion(models.Model):
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="to_user")
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="from_user")
    rating = models.IntegerField(choices=rating_choices)
    description = models.TextField(max_length=500)
    list_date = models.DateTimeField(default=datetime.now)

    class Meta:
        unique_together = ("to_user", "from_user")

    def __str__(self):
        return '{}\'s opinions'.format(self.to_user.username)