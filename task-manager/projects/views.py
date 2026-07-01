from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Profile
from .models import Project
from .serializers import ProjectSerializer
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)

        return Project.objects.filter(
            company=profile.company
        )

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)

        serializer.save(
            company=profile.company
        )