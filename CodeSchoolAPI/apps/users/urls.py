from django.urls import path, include
from rest_framework import routers
from .views import *

p = 'profile/'
urlpatterns = [
        #USER
    path(f'register/',RegisterViewSet.as_view(), name='user_register'),
    path(f'login/', LoginAPiViewSet.as_view(), name='user_login'),
    path(f'list/', UsersListViewSet.as_view(), name='user_list'),
        #PROFILE
    path(f'{p}create/', UserProfileCreateViewSet.as_view(), name='create_profile'),
    path(f'{p}list/', UserProfileListViewSet.as_view(), name='list_profile'),
    path(f'{p}detail/<int:pk>/', UserProfileDetailViewSet.as_view(), name='change_profile'),

]