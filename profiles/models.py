from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, default='', null=True, blank=True)
    avatar = models.ImageField(upload_to='profile_pic/photos/%Y/%m/%d/', default='profile_pic/avatar.png', blank=True)
    bio = models.TextField(max_length=1200, default='', blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    gender_tuple = (('Male', 'Male'), ('Female', 'Female'))
    gender = models.CharField(max_length=10, choices=gender_tuple, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


    


    
