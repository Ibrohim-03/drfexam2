from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from .models import Profile, Avatar
from .serializers import ProfileSerializer, AvatarSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'first_name', 'last_name']

    def update(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile.user != request.user:
            return Response({"detail": "Нет прав на редактирование."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user.profile)

    def destroy(self, request, *args, **kwargs):
        avatar = self.get_object()
        if avatar.profile.user != request.user:
            return Response({"detail": "Нельзя удалять чужие аватары."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)