from django.db import models

from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.name
