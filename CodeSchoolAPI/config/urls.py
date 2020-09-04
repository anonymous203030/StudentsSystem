
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/certificates/', include('apps.certificates.urls')),
    path('api/v1/lectures/', include('apps.lecture.urls')),
    path('api/v1/waitlist/', include('apps.waitlist.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
