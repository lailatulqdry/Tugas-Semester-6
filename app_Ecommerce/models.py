from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    gambar = models.ImageField(upload_to='gambarProduk/', blank=True, null=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    deskripsi = models.TextField()
    warna = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.nama

class CheckOut(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
    tanggal_checkout = models.DateTimeField(auto_now_add=True)
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.jumlah
    
    def save(self, *args, **kwargs):
        # Kurangi stok produk sebelum menyimpan checkout
        if self.product.stock >= self.quantity:
            self.product.stock -= self.quantity
            self.product.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Stock Habis")
    
    def save(self, *args, **kwargs):
        # Hitung total harga berdasarkan harga produk dan jumlah yang dibeli
        self.total_harga = self.product.harga * self.jumlah
        super().save(*args, **kwargs)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=(
        ('bank_transfer', _('Bank Transfer')),
        ('cash', _('Cash')),
    ))
    status = models.CharField(max_length=20, choices=(
        ('pending', _('Pending')),
        ('success', _('Success')),
        ('failed', _('Failed')),
        ('cancelled', _('Cancelled')),
    ))
    payment_time = models.DateTimeField(auto_now_add=True)

    # Methods
    def __str__(self):
        return self.payment_method

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

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def _str_(self):
        return self.email