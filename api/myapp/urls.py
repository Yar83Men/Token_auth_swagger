from django.urls import path, include

# /rest-auth/registration/ (POST)
#
# username
# password1
# password2
# email

# /rest-auth/login/ (POST)
#
# username
# email
# password
# Returns Token key

# /rest-auth/user/ (GET, PUT, PATCH)
#
# username
# first_name
# last_name
# Returns pk, username, email, first_name, last_name

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import UserList, UserDetail

schema_view = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='v1',
      description="Test description",
      terms_of_service="/",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    #path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
