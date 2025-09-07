from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User
from .models import Tasks

class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="u@example.com", name="U", password="pass1234")
        resp = self.client.post(reverse("login"), {"email": "u@example.com", "password": "pass1234"}, format='json')
        token = resp.json()["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_create_task(self):
        resp = self.client.post("/api/tasks/", {"title":"t1","description":"d"}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_owner_only_delete(self):
        # create task by user1
        task = Tasks.objects.create(user=self.user, title="task1")
        # create another user and try deleting using their credentials
        Other = User.objects.create_user(email="other@example.com", name="O", password="pass2345")
        other_resp = self.client.post(reverse("login"), {"email":"other@example.com","password":"pass2345"}, format='json')
        other_token = other_resp.json()["access"]
        # now call delete with other_token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {other_token}")
        delete_resp = self.client.delete(f"/api/tasks/{task.id}/")
        self.assertEqual(delete_resp.status_code, status.HTTP_403_FORBIDDEN)
