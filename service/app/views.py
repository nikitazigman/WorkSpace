import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .filters import TaskFilterSet, UserFilterSet
from .models import Day, Task
from .serializers import (
    DayCreateSerializer,
    DaySerializer,
    TaskCreateSerializer,
    TaskSerializer,
    RegisterSerializer,
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class Register(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class DayList(generics.ListAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilterSet


class DayCreate(generics.CreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DayCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)


class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilterSet


class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailed(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilterSet
