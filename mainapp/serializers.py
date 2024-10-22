from rest_framework import serializers

from .models import User, Task

#====================================================================
# User Serializer: Doesn't include other fields since we dont have
# complete authentication features in this app
#====================================================================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile']

#====================================================================
# Task Serializer: with referenced users
# Note: If you don't want to see all the users a task is assigned to 
#       in the task details then comment out the user line and remove 
#       user from the fields list
#====================================================================
class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'task_type', 'status', 'created_at', 'completed_at', 'user']

#====================================================================
# Task Serializer: without referenced users (for task creation)
#====================================================================
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description']

    #----------------------------------------------------------------
    # To return id as well once the task is created
    #----------------------------------------------------------------
    def to_representation(self, instance):
        return {
            'id'         : instance.id,
            'name'       : instance.name,
            'description': instance.description,
        } 