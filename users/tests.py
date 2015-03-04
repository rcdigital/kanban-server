"""

Tests for kanban API

"""
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from users.models import KanbanUsers
from users.serializers import UsersSerializer 
import json

class UsersTestCase(APITestCase):
    client = APIClient()
    def test_check_user_post(self):
        """
            Ensure we can insert users object.
        """
        data = {'id': 1,'name': 'optimus primal', 'email': 'optimus.primal@transformers.com'}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_check_user_list(self):
        """
            Retrieve user list.
        """
        user = KanbanUsers(name='optimus', email='a@a.com')
        user.save()
        user_list = UsersSerializer(KanbanUsers.objects.all(), many= True)
        response = self.client.get('/api/users/')
        self.assertEqual(response.data, user_list.data)

    def test_save_company(self):
        """
            Create new company
        """

        data = {'id': 1,'name': 'optimus primal', 'email': 'optimus.primal@transformers.com'}
        response = self.client.post('/api/users/', data, format='json')

        data = {'id': 1, 'name': 'RC Digital', 'owner': response.data['id']}
        response = self.client.post('/api/users/'+ str(response.data['id']) +'/companies/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_company(self):
        """
            Retrive user companies
        """

        data = {'id': 1,'name': 'optimus primal', 'email': 'optimus.primal@transformers.com'}
        user_response = self.client.post('/api/users/', data, format='json')

        data = {'id': 1, 'name': 'RC Digital', 'owner': user_response.data['id']}
        response = self.client.post('/api/users/'+ str(user_response.data['id']) +'/companies/', data, format='json')


        response = self.client.get('/api/users/'+ str(user_response.data['id']) +'/companies/', format='json')
        self.assertEqual(response.status_code, 200)
