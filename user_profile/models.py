from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    occupation = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=100)
    street_number = models.CharField(max_length=10)
    flat_number = models.CharField(max_length=10, blank=True)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
