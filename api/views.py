from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .serializers import AutoSerializer, RenterSerializer
from .models import Auto, Renter


class RenterView(ModelViewSet):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class AutoView(ModelViewSet):
    queryset = Auto.objects.all().order_by('created_at')
    serializer_class = AutoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
