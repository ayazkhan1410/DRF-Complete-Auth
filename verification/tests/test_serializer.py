from verification.models import CustomUser as User
from verification.serializers import *
from rest_framework.test import APITestCase

class RegistrationFormSerializerTestCase(APITestCase):
    
    def test_registration(self):
        data = {
            "name": "testname",
            "email": "testmail@gmail.com",
            "password": "testpassword@123",
            "password2": "testpassword@123",
            "tc": True
        }
        serializer = RegistrationFormSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

class LoginFormSerializerTestCase(APITestCase):
    
    def test_login(self):
        data = {
            "email": "testmail@gmail.com",
            "password": "testpassword@123"
        }
        serializer = LoginFormSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

class ProfileSerializerTestCase(APITestCase):
    
    def test_profile(self):
        data = {
            "id": 1,
            "name": "testname",
            "email": "testmail@gmail.com",
            "password": "testpassword@123"
        }
        serializer = ProfileSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})
        
class ChangePasswordSerializerTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            email="testmail@gmail.com",
            name="testname",
            password="oldpassword@123",
            tc=True
        )

    def test_change_password(self):
        data = {
            "password": "newpassword@123",
            "password2": "newpassword@123"
        }
        serializer = ChangePasswordSerializer(data=data, context={'user': self.user})
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

class RestPasswordSerializerTestCase(APITestCase):
    
    def setUp(self):
        # Creating a test user
        self.user = User.objects.create_user(
            email="testmail@gmail.com",
            name="testname",
            password="testpassword@123",
            tc=True
        )

    def test_reset_password(self):
        data = {
            "email": "testmail@gmail.com"
        }
        serializer = RestPasswordSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)  
        self.assertEqual(serializer.errors, {})

class PasswordRestSerializerTestCase(APITestCase):
    
    def setUp(self):
        # Creating a test user
        self.user = User.objects.create_user(
            email="testmail@gmail.com",
            name="testname",
            password="testpassword@123",
            tc=True
        )
    
    def test_password_reset(self):
        data = {
            "password": "newpassword@123",
            "password2": "newpassword@123"
        }
        serializer = PasswordRestSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})
        
