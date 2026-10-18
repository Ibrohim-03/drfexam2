from rest_framework import generics, permissions
from .models import Account
from .serializers import AccountRegistrationSerializer, AccountSerializer

class RegisterView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user