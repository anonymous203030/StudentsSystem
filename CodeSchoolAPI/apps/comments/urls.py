from django.urls import path

from .views import CommentCreateViewSet, CommentListViewSet, CommentDetailViewSet

urlpatterns = [
    path('create/', CommentCreateViewSet.as_view()),
    path('list/', CommentListViewSet.as_view()),
    path('detail/<int:pk>/', CommentDetailViewSet.as_view()),

]