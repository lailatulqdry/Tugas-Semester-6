from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

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
    
    def __str__(self):
        return self.nama



class CheckOut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
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

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
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
        ('approved', _('Approved')),
        ('rejected', _('Rejected')),
    ), default='pending')
    payment_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Logika untuk menetapkan status berdasarkan metode pembayaran
        if self.payment_method == 'cash':
            # Logika untuk menetapkan status 'approved' atau 'rejected' untuk pembayaran cash
            self.status = 'rejected'  
        elif self.payment_method == 'bank_transfer':
            # Logika untuk menetapkan status 'pending' untuk pembayaran bank transfer
            self.status = 'pending'
        super().save(*args, **kwargs)
    def __str__(self):
        return self.payment_method

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlists')

    def __str__(self):
        return f"Wishlist item {self.id} for {self.user.username}"
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('app_Ecommerce.Product', on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s Cart"