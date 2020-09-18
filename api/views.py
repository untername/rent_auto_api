from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .serializers import AutoSerializer, RenterSerializer
from .models import Auto, Renter
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


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


class UpdatedToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'email': user.email
        })
