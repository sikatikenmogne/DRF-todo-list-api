from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.
    """

    class Meta:
        model = Task
        fields = ["id", "title", "description", "closed"]

    def validate_closed(self, value):
        """
        Validate the 'closed' field to ensure it is False.

        Args:
            value (bool): The value of the 'closed' field.

        Raises:
            serializers.ValidationError: If the 'closed' field is True.

        Returns:
            bool: The validated value of the 'closed' field.
        """
        if value is True:
            raise serializers.ValidationError("The finished attrribute must be False")
        return value


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        """
        Meta class for UserSerializer.
        """

        model = User
        fields = ["username", "email", "password"]
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(), fields=["username", "email"]
            )
        ]

    def create(self, validated_data):
        """
        Create a new User instance.

        Args:
            validated_data (dict): The validated data containing user information.

        Returns:
            User: The created User instance.
        """
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        user.save()
        return user
