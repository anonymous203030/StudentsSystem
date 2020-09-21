from django.urls import path, include
from rest_framework import routers

from .views import LectureListViewSet, LectureCreateViewSet, SubscriptionListViewSet, \
    SubscriptionCreateViewSet, SubscriptionDeleteViewSet, LectureDeleteViewSet, CustomLectureListViewSet

s = 'subscription'
urlpatterns = [
    path('list/', LectureListViewSet.as_view()),
    path('create/', LectureCreateViewSet.as_view()),
    path('delete/', LectureDeleteViewSet.as_view()),
    path('custom/', CustomLectureListViewSet.as_view()),

    path(f'{s}/list/', SubscriptionListViewSet.as_view()),
    path(f'{s}/create/', SubscriptionCreateViewSet.as_view()),
    path(f'{s}/delete', SubscriptionDeleteViewSet.as_view()),

]