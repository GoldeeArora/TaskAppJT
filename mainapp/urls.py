from django.urls import path

from .views import TaskCreateView, AssignTaskToUserView, UserTasksView

urlpatterns = [
    path('tasks/create/'             , TaskCreateView.as_view()      , name='task-create'),
    path('tasks/<int:pk>/assign/'    , AssignTaskToUserView.as_view(), name='assign-task'),
    path('users/<int:user_id>/tasks/', UserTasksView.as_view()       , name='user-tasks' ),
]
