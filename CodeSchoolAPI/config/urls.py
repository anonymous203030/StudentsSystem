
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

f = 'api/v1/'
urlpatterns = [
    path('admin/', admin.site.urls),
    #
    path(f'{f}users/', include('apps.users.urls')),
    path(f'{f}certificates/', include('apps.certificates.urls')),
    path(f'{f}lectures/', include('apps.lecture.urls')),
    path(f'{f}waitlist/', include('apps.waitlist.urls')),
    path(f'{f}comments/', include('apps.comments.urls')),
    #
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

