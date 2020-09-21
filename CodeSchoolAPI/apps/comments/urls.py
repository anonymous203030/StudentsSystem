from django.urls import path

from .views import CommentCreateViewSet, CommentListViewSet, CommentDetailViewSet, CustomCommentListViewSet, \
    CommentRelationshipDeleteViewSet, CommentRelationshipCreateViewSet, CommentRelationshipListViewSet

r = 'relationship'

urlpatterns = [
    path('create/', CommentCreateViewSet.as_view()),
    path('list/', CommentListViewSet.as_view()),
    path('detail/<int:pk>/', CommentDetailViewSet.as_view()),
    path('custom/', CustomCommentListViewSet.as_view()),

    path(f'{r}/create/', CommentRelationshipCreateViewSet.as_view()),
    path(f'{r}/list/', CommentRelationshipListViewSet.as_view()),
    path(f'{r}/delete/<int:pk>', CommentRelationshipDeleteViewSet.as_view()),

]