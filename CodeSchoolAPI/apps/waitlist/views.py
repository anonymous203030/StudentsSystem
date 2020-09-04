from django.shortcuts import render
from rest_framework import viewsets

from .models import WaitlistEntry
from .serializers import WaitlistSerializer
from rest_framework.permissions import IsAdminUser

class WaitlistViewSet(viewsets.ModelViewSet):
    queryset = WaitlistEntry.objects.all()
    serializer_class = WaitlistSerializer