from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import Users
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UsersSerializer

class UsersListCreateView(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class= UsersSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsOwnerProfileOrReadOnly,IsAuthenticated]