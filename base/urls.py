from django.urls import path
# from . import views
from .views import TaskCreate, TaskDelete, TaskDetail, TaskList, TaskUpdate, TodoListLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('', views.taskList, name='tasks'),
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("create-task/", TaskCreate.as_view(), name="create-task"),
    path("edit-task/<int:pk>/", TaskUpdate.as_view(), name="edit-task"),
    path("edit-delete/<int:pk>/", TaskDelete.as_view(), name="delete-task"),
    path("login/", TodoListLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]
