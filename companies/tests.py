from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from users.models import KanbanUsers
from users.serializers import UsersSerializer 
from companies.models import Members

# Create your tests here.

def simulate_insert_data():
    client = APIClient()
    data = {'id': 1,'name': 'optimus primal', 'email': 'optimus.primal@transformers.com'}
    user_response = client.post('/api/users/', data, format='json')

    data = {'id': 2,'name': 'Billy', 'email': 'billy@ppr.com'}
    user_response = client.post('/api/users/', data, format='json')

    data = {'id': 3,'name': 'Jason', 'email': 'json@ppr.com'}
    user_response = client.post('/api/users/', data, format='json')

    data = {'id': 1, 'name': 'RC Digital', 'owner': user_response.data['id']}
    client.post('/api/users/'+ str(user_response.data['id']) +'/companies/', data, format='json')

    data = {'id': 1, 'company': 1, 'member': 3}
    client.post('/api/company/1/members/', data, format='json')

    data = {'id': 2, 'company': 1, 'member': 1}
    client.post('/api/company/1/members/', data, format='json')

    data = {'id': 3, 'company': 1, 'member': 2}
    client.post('/api/company/1/members/', data, format='json')

    data = {'id': 1, 'name': 'Development', 'color': '#f00', 'company': 1}
    client.post('/api/company/1/roles/', data, format='json')

class CompanyMembersList(APITestCase):
    client = APIClient()

    def test_members_list(self):
        """
            Retrieve Company Members list based on logged user
        """
        simulate_insert_data()
        response = self.client.get('/api/company/1/members/', format= 'json')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_member(self):
        """
            Retrieve specific member
        """
        simulate_insert_data()
        response = self.client.get('/api/company/1/member/2/', format= 'json')
        self.assertEqual(response.status_code, 200)

class CompanyRoles(APITestCase):
    client = APIClient()
    def test_insert_role(self):
        """
           Insert new company role 
        """
        simulate_insert_data()
        data = {'id': 1, 'name': 'Development', 'color': '#f00', 'company': 1}
        response = self.client.post('/api/company/1/roles/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_roles_list(self):
        """
           Retrieve company roles 
        """
        simulate_insert_data()
        response = self.client.get('/api/company/1/roles/', format='json')
        self.assertEqual(response.status_code, 200)
