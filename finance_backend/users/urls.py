from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

#For user management
router=DefaultRouter()

router.register('', UserViewSet, basename='users')

#For Auth
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns+=router.urls

