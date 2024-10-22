from django.shortcuts        import get_object_or_404
from rest_framework          import status
from rest_framework.response import Response
from rest_framework.views    import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView

from .models      import Task, User
from .serializers import TaskSerializer, TaskCreateSerializer, UserSerializer

#====================================================================
# Create Tasks View: 
# Inputs  - name, description 
# Outputs - 
#====================================================================
class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    def perform_create(self, serializer):
        serializer.save()

#====================================================================
# Create Tasks View: 
# Inputs  - name, description 
# Outputs - 
#====================================================================
class AssignTaskToUserView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        user_ids = request.data.get('user_ids', [])
        users = User.objects.filter(id__in=user_ids)
        task.user.set(users)
        return Response({'message': 'Task assigned successfully'}, status=status.HTTP_200_OK)

#====================================================================
# Create Tasks View: 
# Inputs  - name, description 
# Outputs - 
#====================================================================
class UserTasksView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        return Task.objects.filter(user=user)
