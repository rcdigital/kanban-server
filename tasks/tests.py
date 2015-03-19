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

    data = {'name': 'my first task', 'story': 1, 'estimate_time': 8, 'created_by': 1 }
    client.post('/api/backlog/1/story/1/tasks/', data, format='json')

    data = {'name': 'my second task', 'story': 1, 'estimate_time': 6, 'created_by': 1 }
    client.post('/api/backlog/1/story/1/tasks/', data, format='json')

    data = {'name': 'my third task', 'story': 1, 'estimate_time': 6, 'created_by': 1 }
    client.post('/api/backlog/1/story/1/tasks/', data, format='json')

    data = {'name': 'foo', 'story': 1, 'estimate_time': 8, 'status': 'doing', 'created_by': 1 }
    client.post('/api/backlog/1/story/1/tasks/', data, format='json')

    data = {'name': 'bar', 'story': 1, 'estimate_time': 6, 'status': 'doing', 'created_by': 1 }
    client.post('/api/backlog/1/story/1/tasks/', data, format='json')

    data = {'name': 'zoo', 'story': 1, 'estimate_time': 6, 'status': 'doing', 'created_by': 1 }
    client.post('/api/backlog/1/story/1/tasks/', data, format='json')

    data = {'name': 'foo', 'story': 1, 'estimate_time': 8, 'status': 'done', 'created_by': 1 }
    client.post('/api/backlog/1/story/1/tasks/', data, format='json')

    data = {'name': 'bar', 'story': 1, 'estimate_time': 6, 'status': 'done', 'created_by': 1 }
    client.post('/api/backlog/1/story/1/tasks/', data, format='json')

    data = {'name': 'zoo', 'story': 1, 'estimate_time': 6, 'status': 'done', 'created_by': 1 }
    client.post('/api/backlog/1/story/1/tasks/', data, format='json')

client = APIClient()
class GroupTasks(APITestCase):
    def test_create_task (self):
        simulate_insert_data()
        data = {'name': 'my first task', 'story': 1, 'estimate_time': 8, 'created_by': 1 }
        response = client.post('/api/backlog/1/story/1/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tasks (self):
        simulate_insert_data()
        response = client.get('/api/backlog/1/story/1/tasks/',  format='json')
        self.assertEqual(response.status_code, 200)

    def test_change_status(self):
        simulate_insert_data()
        data = {'status': 'doing'}
        response = client.put('/api/backlog/1/story/1/task/1/data/', data, format= 'json')
        self.assertEqual(response.status_code, 200)

    def test_change_estimate_time(self):
        simulate_insert_data()
        data = {'estimate_time': 12}
        response = client.put('/api/backlog/1/story/1/task/1/data/', data, format= 'json')
        self.assertEqual(response.status_code, 200)

    def test_change_finish_time(self):
        simulate_insert_data()
        data = {'finish_time': 8}
        response = client.put('/api/backlog/1/story/1/task/1/data/', data, format= 'json')
        self.assertEqual(response.status_code, 200)

    def test_change_doing_by(self):
        simulate_insert_data()
        data = {'doing_by': 2}
        response = client.put('/api/backlog/1/story/1/task/1/data/', data, format= 'json')
        response = client.get('/api/backlog/1/story/1/task/1/data/', format = 'json')
        self.assertEqual(response.status_code, 200)

    def test_change_task_story(self):
        simulate_insert_data()
        data = {'story': 2}
        response = client.put('/api/backlog/1/story/1/task/1/data/', data, format= 'json')
        response = client.get('/api/backlog/1/story/1/task/1/data/', format = 'json')
        self.assertEqual(response.status_code, 200)
