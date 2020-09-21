from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .filters import IsOwnerFilter
from .models import Comment, CommentRelationship
from .permissions import IsOwner
from .serializers import CommentSerializer, CommentRelationshipSerializer


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

class CommentRelationshipCreateViewSet(generics.CreateAPIView):
    queryset = CommentRelationship.objects.all()
    serializer_class = CommentRelationshipSerializer
    permission_classes = (IsAuthenticated, )


class CommentRelationshipListViewSet(generics.ListAPIView):
    queryset = CommentRelationship.objects.all()
    serializer_class = CommentRelationshipSerializer
    permission_classes = (IsAuthenticated, )


class CommentRelationshipDeleteViewSet(generics.DestroyAPIView):
    queryset = CommentRelationship.objects.all()
    serializer_class = CommentRelationshipSerializer
    permission_classes = (IsOwner, )


class CustomCommentListViewSet(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (IsOwnerFilter, )
