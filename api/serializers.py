from rest_framework import serializers
from .models import Task, User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'password'

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user