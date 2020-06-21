from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'Tasks'

router = routers.DefaultRouter()
router.register('task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
]
