from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import get_token, signup, current_user
from users.views import UserCreateViewSet

router = DefaultRouter()

router.register('v1/users', UserCreateViewSet)

urlpatterns = [
    path('v1/users/me/', current_user),
    path('', include(router.urls)),
    path('v1/auth/token/', get_token),
    path('v1/auth/signup/', signup),
]
