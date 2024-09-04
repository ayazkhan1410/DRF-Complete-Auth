from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from .renderers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegistrationFormView(APIView):
    # Custom Json Renderer
    renderer_classes = [UserRenderers]
    
    def post(self, request, format=None):
        serializer = RegistrationFormSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({
                "token":token,
                "Message": "Registration Successful",
                },
                status = status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginFormView(APIView):
    renderer_classes = [UserRenderers]
    
    def post(self, request, format=None):
        data = request.data
        serializer = LoginFormSerializer(data=data)
        
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)
            
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({
                    "token":token,
                    "Message": "Login Successful"
                }, status=status.HTTP_200_OK)
            else:
               return Response({"errors":
                   {'non_field errors':['Email or Password is not valid']}
                   }, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({
                "Error": serializer.errors
            }, status= status.HTTP_400_BAD_REQUEST)
            
class ProfileView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        serializer = ProfileSerializer(request.user)
        return Response({
            "profile": serializer.data
        }, status=status.HTTP_200_OK)

class ChangePasswordView(APIView):
    renderer_classes = [UserRenderers]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        
        serializer = ChangePasswordSerializer(data=request.data,context = {
            "user": request.user
        })
        
        if serializer.is_valid(raise_exception=True):
            return Response({
                "Message": "Password Changed Successful",
                },
                status = status.HTTP_200_OK
            )
        else:
            return Response({
                "Error": serializer.errors
            }, status= status.HTTP_400_BAD_REQUEST)
            
class RestPasswordView(APIView):
    renderer_classes = [UserRenderers]
    
    def post(self, request, format=None):
        data = request.data
        serializer = RestPasswordSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response({
                "Msg": "Link send successfully check email"
            })
        else:
            return Response({
                "Error": serializer.errors
            }, status= status.HTTP_400_BAD_REQUEST)
        

class PasswordRestView(APIView):
    renderer_classes = [UserRenderers]
    
    def post(self, request, uid, token, format=None):
        data = request.data
        serializer = PasswordRestSerializer(data=data, context={"uid":uid,"token":token,"user":request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({
                "Message":"password Changed"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "Error": serializer.errors
            }, status= status.HTTP_400_BAD_REQUEST)
            