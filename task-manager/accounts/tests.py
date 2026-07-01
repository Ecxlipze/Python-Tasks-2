from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Company
from django.contrib.auth.models import User


class SignupTest(APITestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="Test Company"
        )

    def test_signup(self):
        url = reverse("signup")

        data = {
            "username": "john",
            "email": "john@example.com",
            "password": "Password123!",
            "company": self.company.id,
            "role": "EMPLOYEE",
        }

        response = self.client.post(
            url,
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        
class LoginTest(APITestCase):

    def setUp(self):
        User.objects.create_user(
            username="rohan",
            password="Password123!"
        )

    def test_login(self):

        url = reverse("token_obtain_pair")

        response = self.client.post(
            url,
            {
                "username": "rohan",
                "password": "Password123!",
            },
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertIn("access", response.data)