from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)

        except ValidationError:
            raise ValueError(_('You Must Provide a Valid Email Address!!'))
    
    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        if not username:
            raise ValueError('User Must Submit a username')
        
        if not first_name:
            raise ValueError('User Must Submit a First Name')
        
        if not last_name:
            raise ValueError('User Must Submit a Last Name')
        
        if email:
            email = self.normalize_email(email=email)
            self.email_validator(email=email)
        else:
            raise ValueError(_('Base User Account: An email address is required'))
        
        user = self.model(username=username, first_name=first_name, last_name=last_name,
                          email=email, **extra_fields)
        user.set_password(password)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_active', True)

        if extra_field.get('is_staff') is not True:
            raise ValueError(_('superusers must have is_staff=True'))
        
        if extra_field.get('is_superuser') is not True:
            raise ValueError(_('superusers must have is_superuser=True'))
        
        if not password:
            raise ValueError(_('superuser must have a password'))
        
        if email:
            email = self.normalize_email(email=email)
            self.email_validator(email=email)
        else:
            raise ValueError(_('Admin Account: An email address is required'))
        
        user = self.create_user(username=username,first_name=first_name, last_name=last_name,email=email, **extra_fields)
        user.save(using=self._db)
        return user