from django.shortcuts import render

from rest_framework import viewsets, generics, filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .filters import IsOwnerFilter
from .models import Lecture, Subscription
from .serializers import LectureSerializer, SubscriptionSerializer
from .permissions import IsOwner


class LectureListViewSet(generics.ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date']
    search_fields = ['title', 'description', 'lecturer_name']


class LectureCreateViewSet(generics.CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsAdminUser]


class LectureDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsAdminUser]


class SubscriptionListViewSet(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['user', 'lecture']
    filterset_fields = ['rating', 'lecture__date', 'reacted_at']
    ordering_fields = ['rating', 'reacted_at']


class SubscriptionCreateViewSet(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class SubscriptionDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]


class CustomLectureListViewSet(ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [IsOwnerFilter, filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'description', 'lecturer_name', 'date']
    ordering_fields = ['id', 'date']
    filterset_fields = ['date', ]
