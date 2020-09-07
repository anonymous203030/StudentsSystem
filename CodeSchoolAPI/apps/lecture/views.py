from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Lecture
from .serializers import LectureSerializer


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = (IsAdminUser, )


