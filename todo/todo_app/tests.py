from django.test import TestCase
from django.urls import reverse  # new
from rest_framework import status  # new
from rest_framework.test import APITestCase
# new
from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title="Learn Javascript",
            body="Ok i will"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "Learn Javascript")
        self.assertEqual(self.todo.body, "Ok i will")
        self.assertEqual(str(self.todo), "Todo object (1)")

    def test_api_listview(self):  # new
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):  # new
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "First Todo")
