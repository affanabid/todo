from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# # Create your models here.



class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True)
    status = models.BooleanField(default=False)  # True if completed, False if not
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


