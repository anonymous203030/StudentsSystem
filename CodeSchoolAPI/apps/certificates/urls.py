from django.urls import path, include
from rest_framework import routers
from .views import CertificatesViewSet

router = routers.DefaultRouter()
router.register(r'', CertificatesViewSet)

urlpatterns = [
    path('', include(router.urls))

]