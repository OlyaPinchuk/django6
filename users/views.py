from rest_framework.generics import ListCreateAPIView, get_object_or_404, CreateAPIView
from django.contrib.auth import get_user_model

from .serializers import UserSerializer
from user_profile.serializers import ProfileSerializer

UserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class AddProfileView(CreateAPIView):
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        serializer.save(user=user)

