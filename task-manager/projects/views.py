from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from accounts.models import Profile
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from audit.models import AuditLog
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "name",
        "description",
    ]
    filterset_fields = [
    "is_active",
    ]
    ordering_fields = [
    "name",
    "created_at",
    "updated_at",
    ]
    ordering = [
    "-created_at",
    ]
    
    def get_queryset(self):
        profile = Profile.objects.get(user=self.request.user)

        return (
            Project.objects
            .select_related("company")
            .filter(
                company=profile.company,
                is_deleted=False,
                )
        )

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)

        project = serializer.save(
        company=profile.company
        )

        AuditLog.objects.create(
            user=self.request.user,
            action="CREATE",
            object_type="Project",
            object_id=project.id,
        )        
    def destroy(self, request, *args, **kwargs):
        project = self.get_object()

        project.is_deleted = True
        project.save()

        AuditLog.objects.create(
            user=request.user,
            action="DELETE",
            object_type="Project",
            object_id=project.id,
        )

        return Response(
            {"message": "Project soft deleted successfully."},
            status=status.HTTP_200_OK,
        )
    def perform_update(self, serializer):
        project = serializer.save()

        AuditLog.objects.create(
            user=self.request.user,
            action="UPDATE",
            object_type="Project",
            object_id=project.id,
        )    