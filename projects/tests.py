from rest_framework.test import APIClient, APITestCase
from rest_framework import status

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

    data = {'id': 1 ,'name': 'Kanban Project', 'company': 1 }
    client.post('/api/company/1/projects/', data, format='json')

client = APIClient()

class CompanyProjects(APITestCase):

    def test_create_project(self):
        """
            Create a project.
        """
        simulate_insert_data()
        data = {'id': 1 ,'name': 'Kanban Project', 'company': 1 }
        response = client.post('/api/company/1/projects/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_company_projects(self):
        """
            Retrieve project list.
        """
        simulate_insert_data()
        response = client.get('/api/company/1/projects/', format='json')
        self.assertEqual(response.status_code, 200)

class ProjectDetails(APITestCase):
    def test_edit_project_name(self):
        simulate_insert_data()
        data = {'id': 1, 'name': 'Project Jiban', 'company': 1}
        response = client.put('/api/project/1/', data, format='json')
        self.assertEqual(response.data, data)
        self.assertEqual(response.status_code, 200)

    def test_delete_project(self):
        simulate_insert_data()
        response = client.delete('/api/project/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_project(self):
        simulate_insert_data()
        response = client.get('/api/project/1/', format='json')
        self.assertEqual(response.status_code, 200)
