from django.test import TestCase
from verification.models import CustomUser as User

class UserModelTest(TestCase):
    
    def test_create_user(self):
        email = "testmail@gmail.com"
        name = "testname"
        password = "testpassword@123"
        tc = True
        
        test_obj = User.objects.create_user(email=email, name=name, password=password, tc=tc)
        
        self.assertEqual(test_obj.email, email)
        self.assertEqual(test_obj.name, name)
        self.assertTrue(test_obj.check_password(password))
        
        self.assertTrue(test_obj.is_active)
        self.assertFalse(test_obj.is_admin)
        self.assertTrue(test_obj.tc)
    
class UserManagerTest(TestCase):
    
    def test_has_perm(self):
        user = User(email = "testmail@gmail.com", name="Ayaz Khan")
        self.assertFalse(user.has_perm("perm"))
    
    def test_is_staff(self):
        user = User(email = "test@gmail.com", name="Ayaz Khan")
        self.assertFalse(user.is_staff)