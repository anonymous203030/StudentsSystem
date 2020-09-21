from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .filters import IsOwnerFilter
from .models import Lecture, Subscription
from .serializers import LectureSerializer, SubscriptionSerializer
from .permissions import IsOwner


class LectureListViewSet(generics.ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAdminUser, )
class LectureCreateViewSet(generics.CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAdminUser, )

class LectureDeleteViewSet(generics.DestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAdminUser, )


class SubscriptionListViewSet(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated, )


class SubscriptionCreateViewSet(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated, )

class SubscriptionDeleteViewSet(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated, )

class CustomLectureListViewSet(ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (IsOwnerFilter, )