from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from social_core.tests.backends import test_email
from .models import *
from .serializers import *
import json
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TestUser(TestCase):
    def test_create_user(self):
        count = User.objects.all().count()
        self.user = User.objects.create(email=test_email)
        self.assertEqual(User.objects.all().count(),count + 1)

    def test_user_serializer(self):
        user_1 = User.objects.create_user(email='tests@gmail.com',
                                          password='teststests')
        user_2 = User.objects.create_user(email='tests2@gmail.com',
                                          password='teststests')

        data = UserSerializer([user_1, user_2], many=True).data
        expected = [{
            'id': user_1.id,
            'email': 'tests@gmail.com',
            'is_student': False
        },
        {
            'id': user_2.id,
            'email': 'tests2@gmail.com',
            'is_student': False
        }
    ]
        self.assertEqual(expected, data)


class TestUsers(APITestCase):
    def setUp(self):
        self.User = get_user_model()
        self.count = self.User.objects.count()
        self.password = 'admin'
        self.user = self.User.objects.create_user(email='user@gmail.com', password=self.password)
        self.admin_user = self.User.objects.create_superuser(email='admin@gmail.com', password=self.password)
        self.client = APIClient()

    def test_invalid_list_user(self):
        url_list = reverse('user_list')
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_login_user(self):
        url_login = reverse('user_login')
        data = {
            'email':'user@gmail.com',
            'password':self.password
        }
        data1 = json.dumps(data)
        response = self.client.post(url_login, data1, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)

    def test_invalid_login_user(self):
        url_login = reverse('user_login')
        data = json.dumps({
            'email': 'user@gmail.com'})
        response = self.client.post(url_login, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestProfile(APITestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(email='user@gmail.com', password='rootroot')
        self.admin_user = self.User.objects.create_superuser(email='admin@gmail.com', password='adminadmin')
        self.client = APIClient()

    def test_valid_create_profile(self):
        url_create = reverse('create_profile')
        data = {
            'first_name':'name',
            'last_name':'surname',
            'preferred_name':'test',
            'fb_profile':'fb_profile',
            'github_name':'anonymous203030',
            'current_level':'Junior'
        }
        data1 = json.dumps(data)
        self.client.force_authenticate(self.admin_user)
        response = self.client.post(url_create, data1, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['first_name'], data['first_name'])
        self.assertEqual(response.data['last_name'], data['last_name'])
        self.assertEqual(response.data['preferred_name'], data['preferred_name'])
        self.assertEqual(response.data['fb_profile'], data['fb_profile'])
        self.assertEqual(response.data['github_name'], data['github_name'])
        self.assertEqual(response.data['current_level'], data['current_level'])

    def test_invalid_create_profile(self):
        url_create = reverse('create_profile')
        data = {
            'first_name': 'name',
            'last_name': 'surname',
            'about': 'abot',
            'birthday': '2020-11-11',
            'owner': self.admin_user.id
        }
        data1 = json.dumps(data)
        self.client.force_authenticate(self.admin_user)
        response = self.client.post(url_create, data1, content_type='application/json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_valid_list_user(self):
        url_list = reverse('user_list')
        self.client.force_authenticate(self.user)
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_list_user(self):
        url_list = reverse('user_list')
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_valid_list_profile(self):
        url_list = reverse('list_profile')
        self.client.force_authenticate(self.user)
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_invalid_list_profile(self):
        url_list = reverse('list_profile')
        response = self.client.get(url_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
