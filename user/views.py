from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer

CustomUser = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


class RegisterUser(APIView):
    """
    API endpoint that allows users to register.
    """
    def post(self, request):
        """
        Create a new user.
        """
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(
              refresh.access_token)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainToken(APIView):
    """
    API endpoint that allows users to obtain authentication tokens.
    """
    def post(self, request):
        """
        Obtain token.
        """
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return Response({'error': 'Both email and password are required.'
                             }, status=status.HTTP_400_BAD_REQUEST)

        user = EmailBackend().authenticate(request, username=email,
                                           password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(
              refresh.access_token)})
        else:
            return Response({'error': 'Invalid email or password'},
                            status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    """
    API endpoint that allows users to retrieve their details.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Retrieve user details.
        """
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateUser(APIView):
    """
    API endpoint that allows users to update their details.
    """
    permission_classes = [IsAuthenticated]

    def put(self, request):
        """
        Update user details.
        """
        user = request.user  # Get the authenticated user
        serializer = CustomUserSerializer(user, data=request.data,
                                          partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    """
    API endpoint that allows users to log out.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Logout user.
        """
        # No specific operations to perform during logout
        return Response({'detail': 'Successfully logged out.'},
                        status=status.HTTP_200_OK)
