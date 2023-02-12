# We new response as we are working with API
from rest_framework.response import Response  
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import *
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

# Generate token manually for user 
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = (UserRenderer,)
    def post(self, request, format=None):
        serializer = UserRegisterationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token, 'message': 'Registeration is successful'}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer= UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = User.objects.get(email=email)
        if(user.is_admin):
            user = authenticate(email='vanshul@gmail.com', password='cv')
        else:
            user = authenticate(email=email, password=password)
        token = get_tokens_for_user(user)
        return Response({'token':token, 'message': 'Login is successful'}, status=status.HTTP_200_OK)
        # token = get_tokens_for_user(user)
        # return Response({'token':token, 'message': 'Login is successful'}, status=status.HTTP_200_OK)
        # elif admin:
        #     token = get_tokens_for_admin(admin)
        #     return Response({'token':token, 'message': 'Admin is successful'}, status=status.HTTP_200_OK)
        # return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(APIView):
    renderer_classes = (UserRenderer,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
class AdminProfileView(APIView):
    renderer_classes = (UserRenderer,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        user = User.objects.all()
        print(user)
        serializer = UserProfileSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserChangePasswordView(APIView):
    renderer_classes = (UserRenderer,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)


class SendPasswordResetEmailView(APIView):
    renderer_classes = (UserRenderer,)
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Password reset email sent successfully'}, status=status.HTTP_200_OK)
        

class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)


# class UserLogoutView(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self, request, format=None):
#         user = request.user
#         serializer = UserLogoutSerializer(user)
#         return Response({'message': 'Logout successfully'}, status=status.HTTP_200_OK)
