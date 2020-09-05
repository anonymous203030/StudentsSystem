from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, UserProfileViewSet

router = routers.SimpleRouter()
router.register(r'', UserViewSet)
router.register((r'profiles'), UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]