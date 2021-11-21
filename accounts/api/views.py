# lookup_field araştır
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from accounts.api.permissions import IsOwner
from accounts.api.serializers import UserSerializer

#Abstact User oluştur.
User = get_user_model()


class UserCreateAPIView(CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = UserSerializer

#ListAPIView yerine Mixinleri inherit etmenin amaçları nelerdir ?
#Aktif Userları listele.
class UserListAPIView(ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [IsAuthenticated]


# query seti filtreliyerek ownerı getir
class UserDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [IsOwner]


class UpdatePasswordAPIView(APIView):
    def put(self, request, *args, **kwargs):
        pass
