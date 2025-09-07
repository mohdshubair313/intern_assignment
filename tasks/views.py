from asyncio import Task
from rest_framework import viewsets, permissions
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now, timedelta

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    @action(detail=False, methods=["get"])
    def recent_completed(self, request):
        last_week = now() - timedelta(days=7)
        tasks = Tasks.objects.filter(user=request.user, status="completed", updated_at__gte=last_week)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

