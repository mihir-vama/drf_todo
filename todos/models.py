from django.db import models

class User(models.Model):
    username = models.TextField(unique=True)
    password = models.TextField()

class Todo(models.Model):
    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,
        null=True, related_name='todos')

    def __str__(self):
        return self.title