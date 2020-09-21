from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .filters import IsOwnerFilter
from .models import Comment
from .permissions import IsOwner
from .serializers import CommentSerializer


class CommentCreateViewSet(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )

class CommentListViewSet(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )


class CommentDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsOwner, IsAdminUser, )

class CustomCommentListViewSet(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (IsOwnerFilter, )