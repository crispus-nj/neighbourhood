from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserAccountPermission(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        user =self.model(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, username, email,  password):
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email= self.normalize_email(email),
            password = password
        )
        user.is_admin = True
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)

        return user
        

class UserAccount(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserAccountPermission()

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self,add_label):
        return self.is_admin
