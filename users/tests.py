"""

Tests for kanban API

"""
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from users.models import KanbanUsers

class UsersTestCase(APITestCase):
    client = APIClient()
    def test_check_user_post(self):
        """
            Ensure we can insert users object.
        """
        data = {'id': 1,'name': 'optimus primal', 'email': 'optimus.primal@transformers.com'}
        response = self.client.post('/api/users/add', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_check_user_list(self):
        """
            Retrieve user list.
        """
        user = KanbanUsers(name='optimus', email='a@a.com')
        user.save()
        user_list = list(KanbanUsers.objects.all().values('id', 'name', 'email', 'thumb'))
        response = self.client.get('/api/users/')
        self.assertEqual(response.data, user_list)
