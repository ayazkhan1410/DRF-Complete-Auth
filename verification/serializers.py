from rest_framework import serializers
from .models import CustomUser as User
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .helpers import Helper
import logging

logging = logging.getLogger(__name__)

class RegistrationFormSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(
        style = {'input_type': 'password'}, 
        write_only = True
    )
    
    class Meta:
        model = User
        fields = ['name',  'email', 'password','password2', 'tc']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
                        '+', '=', '{', '}', '[', ']', '|', '\\',
                        ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']
        
        if password != password2:
            raise serializers.ValidationError({
                "Password doesn't match"
            })
            
        if password.isdigit():
            raise serializers.ValidationError("Password must contain at least one letter.")
        
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
         
        if not any(char in special_char for char in password):
            raise serializers.ValidationError("Password must contain at least one special character.")
            
        return data

    # Because we're created Custom User that's why we need to override create method
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
class LoginFormSerializer(serializers.ModelSerializer):
    '''
    Defining email = serializers.EmailField(max_length=255) ensures proper validation 
     of the email field in your serializer
    '''
    email = serializers.EmailField(max_length=255)
    
    class Meta:
        model = User
        fields = ["email", "password"]
    
    
class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id","name", "email", "password"]

class ChangePasswordSerializer(serializers.Serializer):
    
    password = serializers.CharField(
        style = {'input_type': 'password'}, 
        write_only = True
    )
    password2 = serializers.CharField(
        style = {'input_type': 'password'}, 
        write_only = True
    )
    
    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        user = self.context.get('user')
        
        special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
                        '+', '=', '{', '}', '[', ']', '|', '\\',
                        ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']
        
        if password != password2:
            raise serializers.ValidationError({
                "Password doesn't match"
            })
        
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
         
        if not any(char in special_char for char in password):
            raise serializers.ValidationError("Password must contain at least one special character.")
        
        # Set the new password
        user.set_password(password)
        user.save()
        
        
        return data
    
class RestPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(max_length = 255)
    
    class Meta:
        fields = ["email"]
    
    def validate(self, data):
        email = data.get('email')
        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            link = "http://127.0.0.1:12/api/user/password-rest/"+ uid + "/" + token + "/"
            
            # Sending Email
            body =  "Rest Password here:  " + link
            data = {
                "subject":"Rest Password",
                "body":body,
                "to_email":user.email
            }
            Helper.send_custom_email(data)
            
            return data
        else:
            raise serializers.ValidationError("Email Does't exsist")
        
class PasswordRestSerializer(serializers.Serializer):
    
    password = serializers.CharField(
        style = {'input_type': 'password'}, 
        write_only = True
    )
    password2 = serializers.CharField(
        style = {'input_type': 'password'}, 
        write_only = True
    )
    
    class Meta:
        fields = ["password", "password2"]
    
   
class PasswordRestSerializer(serializers.Serializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, 
        write_only=True
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'}, 
        write_only=True
    )

    class Meta:
        fields = ["password", "password2"]

    def validate(self, data):
        try:
            password = data.get('password')
            password2 = data.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_',
                            '+', '=', '{', '}', '[', ']', '|', '\\',
                            ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '`', '~']

            if password != password2:
                raise serializers.ValidationError({
                    "password2": "Password doesn't match"
                })

            if len(password) < 8:
                raise serializers.ValidationError("Password must be at least 8 characters long.")

            if not any(char in special_char for char in password):
                raise serializers.ValidationError("Password must contain at least one special character.")

            # Decode the uid and convert to string, then to an integer
            id = int(urlsafe_base64_decode(uid).decode())
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("Token is expired or invalid")

            # Set the new password
            user.set_password(password)
            user.save()

            return data 
        except DjangoUnicodeDecodeError as identifier:
            raise serializers.ValidationError("Link is invalid")
                    