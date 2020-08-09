from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lists')
    name = models.CharField(max_length=256)
    is_default = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )
    name = models.CharField(max_length=256)
    details = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
