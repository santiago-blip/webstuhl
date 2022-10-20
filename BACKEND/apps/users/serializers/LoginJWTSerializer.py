from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ObtainTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['superUser'] = user.is_superuser
        return token