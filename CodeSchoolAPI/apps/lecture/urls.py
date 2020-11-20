from django.urls import path, include
from rest_framework import routers
from .views import *


s = 'subscription'
urlpatterns = [
    path('list/', LectureListViewSet.as_view(), name='lecture_list'),
    path('create/', LectureCreateViewSet.as_view(), name='lecture_create'),
    path('detail/<int:pk>/', LectureDetailViewSet.as_view(), name='lecture_detail'),
    path('custom/', CustomLectureListViewSet.as_view(), name='lecture_custom'),

    path(f'{s}/list/', SubscriptionListViewSet.as_view(), name='sub_list'),
    path(f'{s}/create/', SubscriptionCreateViewSet.as_view(), name='sub_create'),
    path(f'{s}/detail/<int:pk>/', SubscriptionDetailViewSet.as_view(), name='sub_detail'),

]