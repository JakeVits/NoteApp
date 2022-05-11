from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Note(models.Model):
    owner = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=20, unique=True)
    context = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
