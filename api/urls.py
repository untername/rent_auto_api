from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import RenterView, AutoView
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'cars', AutoView)
router.register(r'renters', RenterView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth')]
