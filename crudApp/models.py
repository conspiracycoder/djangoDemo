from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = str(uuid4())[:30]  # Generate a unique username
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email}, {self.first_name}, {self.last_name}"

