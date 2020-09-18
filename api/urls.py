from rest_framework import routers
from .views import RenterView, AutoView, UpdatedToken
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'cars', AutoView)
router.register(r'renters', RenterView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', UpdatedToken.as_view())]