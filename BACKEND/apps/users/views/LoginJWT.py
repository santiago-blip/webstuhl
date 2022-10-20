from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.serializers.LoginJWTSerializer import ObtainTokenSerializer

class ObtainTokenAccess(TokenObtainPairView):
    serializer_class = ObtainTokenSerializer
