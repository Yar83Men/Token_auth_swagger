from django.contrib.auth.models import User
from rest_framework import generics, mixins
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, pk=None):
        return self.delete(request, pk)