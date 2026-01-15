from django.contrib import admin
from .models import Todo, User


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
