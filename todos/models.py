from django.db import models


class User(models.Model):
    username = models.TextField()
    password = models.TextField()
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL,
        null=True, related_name='todo')

    def __str__(self):
        return self.title