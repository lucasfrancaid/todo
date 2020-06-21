from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows tasks to be viewed or edited.
    '''
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
