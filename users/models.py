from django.contrib.auth.models import AbstractBaseUser,    BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

  def _create_user(self, email, password,username,first_name,last_name,phone,gender,admin_type, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    if not admin_type:
        raise ValueError('Select admin type')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        username=username,
        phone=phone,
        admin_type=admin_type,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self,email, password,username,first_name,last_name,phone,gender,admin_type, **extra_fields):
    return self._create_user(email, password,username,first_name,last_name,phone,gender,admin_type, False, False, **extra_fields)

  def create_superuser(self, email, password,first_name,last_name,gender, **extra_fields):
    user=self._create_user(email, password,"null",first_name,last_name,"null",gender,"null", True, True, **extra_fields)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField( max_length=1000)
    first_name = models.CharField( max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20,unique=False)
    gender=models.CharField(max_length=20)
    admin_type=models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','gender']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)