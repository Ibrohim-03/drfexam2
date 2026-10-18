from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Group, GroupMember
from .serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Group.objects.filter(members__user=self.request.user)

    def perform_create(self, serializer):
        group = serializer.save(owner=self.request.user)
        GroupMember.objects.create(group=group, user=self.request.user, role='owner')

    def destroy(self, request, *args, **kwargs):
        group = self.get_object()
        if group.owner != request.user:
            return Response({"detail": "Только владелец может удалить группу."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)