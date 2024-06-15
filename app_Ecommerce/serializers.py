from rest_framework import serializers
from .models import Category, Product, CheckOut, Review, Payment, CustomUser


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'nama',
            'harga',
            'stock',
            'gambar',
            'warna',
            'available',
            'deskripsi',
        ]

class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = [
            'id',
            'nama',
            'product',
        ]

class CheckoutSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = CheckOut
        fields = [
            'id', 
            'product',
            'jumlah',
            'tanggal_checkout',
            'total_harga',
        ]
    def create(self, validated_data):
        # Ambil data produk yang dibeli dari validated_data
        product_data = validated_data.pop('product')
        product = product_data['product']
        jumlah = product_data.get('jumlah', 1)  # Default 1 jika jumlah tidak disediakan

        # Hitung total harga
        total_harga = product.harga * jumlah

        # Buat entri checkout baru dengan data yang divalidasi
        checkout = CheckOut.objects.create(product=product, jumlah=jumlah, total_harga=total_harga, **validated_data)
        return checkout

class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Review
        fields = [
            'id',
            'product',
            'rating',
            'comment',
            'created_at',
        ]

class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = [
            'id',
            'amount',
            'payment_method',
            'status',
            'payment_time',
        ]

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user