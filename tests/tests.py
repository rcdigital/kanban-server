"""

Tests for kanban API

"""

from rest_framework.test import APIRequestFactory
import unittest
import json

class UrlTestPersistense(unittest.TestCase):
    factory = APIRequestFactory()
    def check_user_urls(self):
        request = factory.post('/api/users/', {'name': 'optimus primal', 'email': 'optimus.primal@transformer.com'}, content_type =  'application/json')

    def __init__(self):
        self.check_user_urls()
