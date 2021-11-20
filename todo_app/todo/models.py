from django.db import models
# Create your models here.

class Todo(models.Model):
    title = models.TextField()
    desc = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    is_done = models.BooleanField(default=False)