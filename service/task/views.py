from rest_framework.viewsets import ModelViewSet
from . import models, serializers, filters


class TaskViewSet(ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    filterset_class = filters.TaskFilterSet

    def perform_create(self, serializer: serializers.TaskSerializer):
        serializer.save(user=self.request.user)
