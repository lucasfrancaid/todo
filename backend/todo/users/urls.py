from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'Users'

router = routers.SimpleRouter()
router.register('users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
