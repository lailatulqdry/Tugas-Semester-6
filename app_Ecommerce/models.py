from django.db import models

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
    jumlah = models.PositiveIntegerField()
    tanggal_checkout = models.DateTimeField(auto_now_add=True)
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.jumlah
    '''
    def save(self, *args, **kwargs):
        # Kurangi stok produk sebelum menyimpan checkout
        if self.product.stock >= self.quantity:
            self.product.stock -= self.quantity
            self.product.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Stock Habis")
    '''
    

    