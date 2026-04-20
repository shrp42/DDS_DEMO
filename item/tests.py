from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class ItemApiTests(APITestCase):
    def test_get_items_list(self):
        url = reverse('api_items_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)