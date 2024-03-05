from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Pup


class PupTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_Pup = Pup.objects.create(
            name="lab",
            owner=testuser1,
            description="medium/large size",
        )
        test_Pup.save()

    def test_Pups_model(self):
        Pup = Pup.objects.get(id=1)
        actual_owner = str(Pup.owner)
        actual_name = str(Pup.name)
        actual_description = str(Pup.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "lab")
        self.assertEqual(
            actual_description, "medium/large size"
        )

    def test_get_Pup_list(self):
        url = reverse("Pup_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Pups = response.data
        self.assertEqual(len(Pups), 1)
        self.assertEqual(Pups[0]["name"], "lab")

    def test_get_Pup_by_id(self):
        url = reverse("Pup_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Pup = response.data
        self.assertEqual(Pup["name"], "lab")

    def test_create_Pup(self):
        url = reverse("Pup_list")
        data = {"owner": 1, "name": "beage", "description": "small"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        Pups = Pup.objects.all()
        self.assertEqual(len(Pups), 2)
        self.assertEqual(Pup.objects.get(id=2).name, "beagle")

    def test_update_Pup(self):
        url = reverse("Pup_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "lab",
            "description": "medium/large size dog",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        Pup = Pup.objects.get(id=1)
        self.assertEqual(Pup.name, data["name"])
        self.assertEqual(Pup.owner.id, data["owner"])
        self.assertEqual(Pup.description, data["description"])

    def test_delete_Pup(self):
        url = reverse("Pup_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        Pups = Pup.objects.all()
        self.assertEqual(len(Pups), 0)
# Create your tests here.
