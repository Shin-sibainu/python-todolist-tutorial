from django.urls import path
# from . import views
from .views import TaskCreate, TaskDetail, TaskList

urlpatterns = [
    # path('', views.taskList, name='tasks'),
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("create-task/", TaskCreate.as_view(), name="create-task"),
]