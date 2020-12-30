from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    # Create a relationship (not an inheritance form User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add additional attributes to user wanted
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics') # sub-directoria in media folder

    def __str__(self):
        return self.user.username # default attribute of User class