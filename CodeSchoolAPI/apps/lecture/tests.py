import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TestLecture(APITestCase):
    def setUp(self):
        user = get_user_model()
        self.password = 'rootroot'
        self.user = user.objects.create_user(email='user@gmail.com', password=self.password)
        self.admin_user = user.objects.create_superuser(email='admin@gmail.com', password=self.password)
        self.client = APIClient()

    def test_valid_lecture_create(self):
        url_create = reverse('lecture_create')
        self.client.force_authenticate(self.admin_user)
        data = {
            'title': 'title',
            'description': 'description',
            'date': '2020-11-11',
            'duration': 120,
            'slides_url': 'url',
            'subscriber': self.user.id,
            'admin_user': self.admin_user.id
        }
        data1 = json.dumps(data)
        response = self.client.post(url_create, data1, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.data['date'], data['date'])
        self.assertEqual(response.data['duration'], data['duration'])
        self.assertEqual(response.data['slides_url'], data['slides_url'])
        self.assertEqual(response.data['admin_user'], data['admin_user'])

    def test_invalid_lecture_create(self):
        url_create = reverse('lecture_create')
        data = {
            'title': 'title',
            'description': 'description',
            'date': '2020-11-11',
            'duration': 120,
            'slides_url': 'url',
            'subscriber': self.user.id,
            'admin_user': self.admin_user.id
        }
        data1 = json.dumps(data)
        response = self.client.post(url_create, data1, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.force_authenticate(self.admin_user)
        data = {
            'title': 'title',
            'description': 'description',
            'date': '2020-11-11',
            'subscriber': self.user.id,
            'admin_user': self.admin_user.id
        }
        data1 = json.dumps(data)
        response = self.client.post(url_create, data1, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_list_lecture(self):
        url_list = reverse('lecture_list')
        self.client.force_authenticate(self.user)
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_list_lecture(self):
        url_list = reverse('lecture_list')
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
