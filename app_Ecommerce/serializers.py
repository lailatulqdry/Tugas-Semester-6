from rest_framework import serializers
from .models import Category, Product, CheckOut, Review, Payment, Wishlist, Cart
from django.contrib.auth.models import User


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
    product = ProductSerializer()
    class Meta:
        model = CheckOut
        fields = [
            'id', 
            'product',
            'jumlah',
            'tanggal_checkout',
            'total_harga',
            'user',
        ]
    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product, created = Product.objects.get_or_create(**product_data)
        checkout = CheckOut.objects.create(product=product, **validated_data)
        return checkout

class ReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Review
        fields = [
            'id',
            'product',
            'rating',
            'comment',
            'created_at',
            'user',
        ]
    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product, created = Product.objects.get_or_create(**product_data)
        review = Review.objects.create(product=product, **validated_data)
        return review
    
    def update(self, instance, validated_data):
        product_data = validated_data.pop('product')
        product = instance.product

        instance.rating = validated_data.get('rating', instance.rating)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()

        product.name = product_data.get('name', product.name)
        product.description = product_data.get('description', product.description)
        product.save()

        return instance

class PaymentSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Payment
        fields = [
            'id',
            'amount',
            'payment_method',
            'status',
            'payment_time',
            'user',
            'product',
        ]

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product, created = Product.objects.get_or_create(**product_data)
        payment = Payment.objects.create(product=product, **validated_data)
        return payment

class UserSerializer(serializers.ModelSerializer):
    CheckOut = CheckoutSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'CheckOut']

class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Wishlist
        fields = [
            'id',
            'user',
            'product',
        ]

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product, created = Product.objects.get_or_create(**product_data)
        wishlist = Wishlist.objects.create(product=product, **validated_data)
        return wishlist

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'product',
            'quantity',
        ]