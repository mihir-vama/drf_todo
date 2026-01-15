from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TodoViewSet


todo_router = DefaultRouter()
todo_router.register("", TodoViewSet, basename="user-todos")

user_router = DefaultRouter()
user_router.register("", UserViewSet, basename="users")

urlpatterns = [
    path("<int:admin_id>/todo/", include(todo_router.urls)),
    path("", include(user_router.urls)),
]
