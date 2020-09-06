from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework import status
from social_core.tests.backends import test_username, test_email

from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from .views import UserProfileViewSet, UserViewSet


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