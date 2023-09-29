from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid;
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=20, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_by_user')
    updated_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_by_user')

    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.username

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='products_created')
    updated_by= models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='products_updated')
    def __str__(self):
        return self.product_name


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.FloatField()
    unit_price = models.FloatField()
    date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='stocks_created')

    def __str__(self):
        return str(self.product)


class StockIn(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.FloatField()
    unit_price = models.FloatField()
    date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='stockins_created')


class StockOut(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.FloatField()
    unit_price = models.FloatField()
    date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='stockouts_created')


class Payment_confirmation(models.Model):
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='payment_confirmations_created')

class Packages(models.Model):
    package_name= models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='package_created')


