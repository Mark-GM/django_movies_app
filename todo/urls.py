from django.urls import path
from .views import *

app_name = "todo"

urlpatterns = [
    path("", index, name="index"),
    # path("task/<int:task_id>/details", todo_details, name="todo-details"),
    path("list", todo_list, name="todo-list"),
    path("task/<int:task_id>/view", todo_details, name="todo-detail"),
    path("task/<int:task_id>/update", todo_update, name="todo-update"),
    path("task/<int:task_id>/delete", todo_delete, name="todo-delete"),
]
