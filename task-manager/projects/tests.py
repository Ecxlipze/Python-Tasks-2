from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import Company, Profile


class ProjectTest(APITestCase):

    def setUp(self):

        self.company = Company.objects.create(
            name="Test Company"
        )

        self.user = User.objects.create_user(
            username="admin",
            password="Password123!"
        )

        Profile.objects.create(
            user=self.user,
            company=self.company,
            role="ADMIN",
        )

        response = self.client.post(
            "/api/token/",
            {
                "username": "admin",
                "password": "Password123!",
            },
        )

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {response.data['access']}"
        )

    def test_create_project(self):

        response = self.client.post(
            "/api/projects/",
            {
                "name": "Website",
                "description": "Company website",
                "is_active": True,
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )