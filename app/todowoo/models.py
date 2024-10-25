from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='todos',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        user = get_current_user()
        self.author = user
        super(Todo, self).save(*args, **kwargs)
