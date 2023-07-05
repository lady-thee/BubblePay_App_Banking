from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

import uuid 



class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        pass
        if not email:
            raise ValueError('Email must be given!')
        
        kwargs.setdefault('is_superuser', False)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', False)
        # kwargs.setdefault('')

        user = self.model(
            email = self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 
    

    def create_superuser(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email must be given')
        
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        kwargs.setdefault('is_staff', True)


        superuser = self.model(
            email = self.normalize_email(email),
            **kwargs
        )
        superuser.set_password(password)
        superuser.save(using=self._db)
        return superuser



class Users(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    email = models.EmailField(max_length=250, unique=True, db_index=True, null=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=250, null=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        unique_together = ['id', 'email']

    def __str__(self):
        return self.email 
    
    def has_perms(self, perm, obj=None):
        return self.is_superuser
    
    def get_full_name(self):
        return self.email
    
    def has_module_perms(self, app_label):
        return True






class Customers(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=200, null=False, blank=False)
    middlename = models.CharField(max_length=200, null=False, blank=False)
    lastname = models.CharField(max_length=200, null=False, blank=False)
    mobile = PhoneNumberField(blank=True, region='NG')
    location = models.CharField(max_length=150, blank=True, null=True)
    photo = models.ImageField(default='', upload_to='photo/%Y/%m/%d')
    BVN = models.CharField(max_length=11, null=False, blank=False)

    def __str__(self) -> str:
        return self.username



class Account(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=None)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=200, null=False, default='')
    account_number = models.CharField(max_length=10, blank=False, null=False)
    balance = models.DecimalField(decimal_places=2, max_digits=10, null=True, default=10000)
    
    

    def __str__(self) -> str:
        return str(self.balance)

