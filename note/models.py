from django.db import models
from django.urls import reverse


class Note(models.Model):
    objects = None
    title = models.CharField(max_length=300, primary_key=True, null=False)
    context = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
