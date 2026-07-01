from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Company, Profile
class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "email", "password"]
    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        write_only=True,
    )
    role = serializers.ChoiceField(
        choices=Profile.Role.choices,
        write_only=True,
    )
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "company",
            "role",
        ]

    def create(self, validated_data):
        company = validated_data.pop("company")
        role = validated_data.pop("role")
        password = validated_data.pop("password")
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        Profile.objects.create(
            user=user,
            company=company,
            role=role,
        )
        return user