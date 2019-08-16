from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import *
from .serializers import *

class UserViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return UserReadSerializer
        return UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(pk=self.request.user.id)
        
    