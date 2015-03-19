from rest_framework.test import APIClient, APITestCase
from rest_framework import status

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

    data = {'id': 1 ,'name': 'Site 1.0', 'project': 1 }
    client.post('/api/project/1/backlogs/', data, format='json')

    data = {'name': 'First Deliver', 'backlog': 1, 'order': 1}
    client.post('/api/backlog/1/stories/', data, format='json')

    data = {'name': 'Secondo Deliver', 'backlog': 1, 'order': 2}
    client.post('/api/backlog/1/stories/', data, format='json')

client = APIClient()

class BacklogList(APITestCase):
    def test_insert_backlog(self):
        """
            Create a backlog.
        """
        simulate_insert_data()
        data = {'id': 1 ,'name': 'Site 1.0', 'project': 1 }
        response = client.post('/api/project/1/backlogs/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_project_backlogs(self):
        """
            List project backlogs.
        """
        simulate_insert_data()
        response = client.get('/api/project/1/backlogs/', format='json')
        self.assertEqual(response.status_code, 200)


class BacklogDetails(APITestCase):
    def test_update_backlog(self):
        """
            update backlog.
        """
        simulate_insert_data()
        data = {'name': 'Site 2.0'}
        response = client.put('/api/project/1/backlog/1/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete_backlog(self):
        """
            delete backlog
        """
        simulate_insert_data()
        response = client.delete('/api/project/1/backlog/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class StoryList(APITestCase):
    def test_insert_story(self):
        """
           Insert new story 
        """
        simulate_insert_data()
        data = {'name': 'First Deliver', 'backlog': 1, 'order': 1}
        response = client.post('/api/backlog/1/stories/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_story_list(self):
        """
           Retrieve sotries 
        """
        simulate_insert_data()
        response = client.get('/api/backlog/1/stories/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_story(self):
        """
           Retrieve story by id 
        """
        simulate_insert_data()
        response = client.get('/api/backlog/1/story/2/', format='json')
        self.assertEqual(response.status_code, 200)

    def test_edit_story_name(self):
        """
           Retrieve sotry by id 
        """
        simulate_insert_data()
        data = {'name': 'Changing story'}
        response = client.put('/api/backlog/1/story/2/', data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_edit_story_name(self):
        """
           edit story name 
        """
        simulate_insert_data()
        data = {'name': 'Changing story', 'order': 3}
        response = client.put('/api/backlog/1/story/2/', data, format='json')
        self.assertEqual(response.status_code, 200)
