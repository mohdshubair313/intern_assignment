from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import User

class UserTests(APITestCase):
    def test_register_user(self):
        url = reverse("register")
        payload = {"email": "t1@example.com", "name": "T1", "password": "testpass123"}
        resp = self.client.post(url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        User.objects.create_user(email="t2@example.com", name="T2", password="testpass123")
        resp = self.client.post(reverse("login"), {"email": "t2@example.com", "password": "testpass123"}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn("access", resp.json())
