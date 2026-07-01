from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from accounts.models import Profile

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()   # <-- Keep this

    serializer_class = TaskSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.profile.role == Profile.Role.ADMIN:
            return Task.objects.select_related(
                "assigned_to",
                "project",
            ).all()
            
        return Task.objects.select_related(
            "assigned_to",
            "project",
        ).filter(
            assigned_to=user
        )

    @action(detail=True, methods=["patch"])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.completed = True
        task.save()

        serializer = self.get_serializer(task)

        return Response(serializer.data)
