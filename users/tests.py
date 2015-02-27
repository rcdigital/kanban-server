"""

Tests for kanban API

"""
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
class UsersTestCase(APITestCase):
    client = APIClient()
    def test_check_user_post(self):
        """
            Ensure we can insert users object.
        """
        data = {'id': 1,'name': 'optimus primal', 'email': 'optimus.primal@transformer.com'}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
