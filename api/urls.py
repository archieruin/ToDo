from django.urls import path

from .views import ListListCreateView
from .views import ListDetailView
from .views import TaskListCreateView
from .views import TaskDetailView

urlpatterns = [
    path('lists/', ListListCreateView.as_view()),
    path('lists/<int:pk>', ListDetailView.as_view()),

    path('tasks/', TaskListCreateView.as_view()),
    path('tasks/<int:pk>', TaskDetailView.as_view()),
]
