from todos.views import CreateAPIView, TodoListAPIView
from django.urls import path

urlpatterns = [
    path('create', CreateAPIView.as_view(), name="create-todo"),
    path('list', TodoListAPIView.as_view(), name="list-todos"),
]