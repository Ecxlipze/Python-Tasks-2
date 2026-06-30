from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Project name cannot be empty."
            )
        return value