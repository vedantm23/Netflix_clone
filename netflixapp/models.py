from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Choices for age limit
AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)

# Choices for movie type
MOVIE_CHOICES = (
    ('seasonal', 'This is a Seasonal Movie'),
    ('single', 'Single'),
)

# Custom user model
class CustomerUser(AbstractUser):
    profiles = models.ManyToManyField('Profile')

# Profile model
class Profile(models.Model):
    name = models.CharField(max_length=1000)
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name  # Ensure this always returns a string

# Movie model
class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField('Video')
    image = models.ImageField(upload_to='covers')
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

    def __str__(self):
        return self.title  # Ensure this always returns a string

# Video model
class Video(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to='movies')

    def __str__(self):
        return self.title  # Ensure this always returns a string
