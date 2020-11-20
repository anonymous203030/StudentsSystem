from django.shortcuts import render
from rest_framework import viewsets

from .models import WaitlistEntry
from .serializers import WaitlistSerializer
from rest_framework.permissions import AllowAny


class WaitlistViewSet(viewsets.ModelViewSet):
    queryset = WaitlistEntry.objects.all()
    serializer_class = WaitlistSerializer
