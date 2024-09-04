from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.mail import EmailMessage
import os

class UserManager(BaseUserManager):
    def create_user(self, email, name,tc, password=None, password2=None):
        """
        Creates and saves a User with the given email,name,tc
        and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,tc, password=None):
        """
        Creates and saves a User with the given email,name,tc
        and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=True
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Helper:
    
    @staticmethod
    def send_custom_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_email']],
        )
        email.send()