from django.urls import path, include
from rest_framework import routers

from .views import LectureListViewSet, LectureCreateViewSet, SubscriptionListViewSet, \
    SubscriptionCreateViewSet

urlpatterns = [
    path('list/', LectureListViewSet.as_view()),
    path('create/', LectureCreateViewSet.as_view()),
    path('subscription/list/', SubscriptionListViewSet.as_view()),
    path('subscription/create/', SubscriptionCreateViewSet.as_view()),

]