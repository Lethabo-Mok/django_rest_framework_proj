# from todos.views import CreateAPIView, TodoListAPIView
from todos.views import TodoAPIView, TodoDetailAPIView
from django.urls import path

urlpatterns = [
    path("",TodoAPIView.as_view(), name="todos"),
    # path('create', CreateAPIView.as_view(), name="create-todo"),
    # path('list', TodoListAPIView.as_view(), name="list-todos"),
    path("<int:id>",TodoDetailAPIView.as_view(), name="todo"),
]