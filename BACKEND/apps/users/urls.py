from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from apps.users.views.LoginJWT import ObtainTokenAccess

urlpatterns = [
    path('login/',ObtainTokenAccess.as_view(),name="obtainToken"),
    path('refresh/',TokenRefreshView.as_view(),name="refreshToken"),
]