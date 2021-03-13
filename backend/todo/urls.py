from django.conf import settings
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'Todo'

schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version='v1',
        description="Documentation for Todo API",
    ),
    public=True,
    url=settings.API_URL,
    urlconf='todo.urls',
    authentication_classes=(JWTAuthentication,),
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include('todo.tasks.urls')),
    path('api/', include('todo.users.urls')),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
