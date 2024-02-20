from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(blank=True, null=True,)
    profile_picture = models.ImageField(upload_to='profile_pictures/',
                                        null=True, blank=True)

    def __str__(self):
        return self.username
