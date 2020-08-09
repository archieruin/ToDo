from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import List, Task
from api.permissions import IsOwnerList
from api.permissions import IsOwnerTask
from . import controllers
from .serializers import ListCreateSerializer
from .serializers import ListListSerializer
from .serializers import ListDetailSerializer
from .serializers import TaskCreateSerializer
from .serializers import TaskListSerializer
from .serializers import TaskDetailSerializer


class ListListCreateView(ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListCreateSerializer
    permission_classes = [IsAuthenticated, IsOwnerList]

    def list(self, request, *args, **kwargs):
        queryset = request.user.lists.all()
        serializer = ListListSerializer(queryset, many=True)
        return Response(serializer.data)


class ListDetailView(RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerList]


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = [IsAuthenticated, IsOwnerTask]

    def list(self, request, *args, **kwargs):
        queryset = controllers.get_user_tasks(request.user)
        serializer = TaskListSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsAuthenticated, IsOwnerTask]
