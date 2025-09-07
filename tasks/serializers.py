from rest_framework import serializers
from .models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"
        read_only_fields = ["user", "created_at", "updated_at"]

    def create(self, validated_data):
        user = self.context['request'].user  # request se current logged in user milega
        return Tasks.objects.create(user=user, **validated_data)