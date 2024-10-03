

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta():
        ordering = ('-publish',)

    def __str__(self):
        return self.title








