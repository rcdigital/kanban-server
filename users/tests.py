"""

Tests for kanban API

"""
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from users.models import KanbanUsers
from users.serializers import UsersSerializer 
import json

def simulate_data_storage():
    client = APIClient()
    data = {'id': 1,'name': 'optimus primal', 'email': 'optimus.primal@transformers.com'}
    client.post('/api/users/', data, format='json')

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

    def test_edit_user_data(self):
        """
            Retrieve user list.
        """
        simulate_data_storage()
        data = {'id': 1, 'name': 'Gandalf The Grey', 'email': 'gdalf@gmail.com', 'thumb': 'null'}
        response = self.client.put('/api/users/1/', data, format='json')
        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, 200)

    def test_delete_user_data(self):
        simulate_data_storage()
        response = self.client.delete('/api/users/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



class UserCompanyTestCase(APITestCase):
    client = APIClient()

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

        data = {'id': 1, 'company': response.data['id'], 'member': user_response.data['id']}

        response = self.client.post('/api/company/'+ str(response.data['id']) +'/member/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_company_data(self):
        """
            Edit company data
        """

