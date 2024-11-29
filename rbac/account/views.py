from .serializers import UserSerializers, UserLoginSerializer
from .models import User, BlacklistedToken
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAdminUser]  # Only admin users can access the user list

    def get_permissions(self):
        if self.request.user.is_staff:  # If the user is an admin, allow them to view the list
            return super().get_permissions()
        else:  # For non-admin users, deny access
            self.permission_classes = [AllowAny]  # Deny access if not an admin
            return super().get_permissions()


class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'email': serializer.data['email'],
                'role': serializer.data['role']
            }

            return Response(response, status=status_code)


class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            # Get the refresh token from the request data
            refresh_token = request.data.get('refresh')

            if not refresh_token:
                return Response({"detail": "Refresh token required."}, status=status.HTTP_400_BAD_REQUEST)

            # Blacklist the refresh token
            BlacklistedToken.objects.create(token=refresh_token)

            response = {
                "success": True,
                "statusCode": status.HTTP_200_OK,
                "message": "Successfully logged out."
            }

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
