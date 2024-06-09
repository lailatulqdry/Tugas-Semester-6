from rest_framework import serializers
from .models import Category, Product, CheckOut


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
    class Meta:
        model = CheckOut
        fields = [
            'id', 
            'jumlah',
            'tanggal_checkout',
            'total_harga',
        ]
    '''
    def create(self, validated_data):
        request = self.context.get('request', None)
        if request:
            validated_data['user'] = request.user
        product_data = validated_data.pop('product')
        product = Product.objects.get(pk=product_data['id'])
        checkout = CheckOut.objects.create(product=product, **validated_data)
        return checkout
    '''
    