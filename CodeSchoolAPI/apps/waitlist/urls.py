from django.urls import path,include
from rest_framework import routers

from .views import WaitlistViewSet

router = routers.SimpleRouter()
router.register(r'', WaitlistViewSet)
urlpatterns = [
    path('', include(router.urls)),
]