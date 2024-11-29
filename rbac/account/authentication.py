# authentication.py
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import BlacklistedToken

class BlacklistJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        auth = super().authenticate(request)
        if not auth:
            return None
        user, auth_token = auth
        try:
            if BlacklistedToken.objects.filter(token=str(auth_token)).exists():
                raise AuthenticationFailed('Token has been blacklisted.')
        except BlacklistedToken.DoesNotExist:
            pass
        return (user, auth_token)
