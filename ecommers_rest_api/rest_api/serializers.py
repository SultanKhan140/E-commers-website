from rest_framework import serializers
from .models import *


class Userserializer(serializers.ModelSerializer):
    class meat:
        model = User
        fields = ['id', 'Username', 'email', 'password',
                  'address', 'phone', 'create_at']


class Storeserializer(serializers.ModelSerializer):
    class meat:
        model = Product
        fields = ['id', 'userId', 'name', 'create_at']


class Productserializer(serializers.ModelSerializer):
    class meat:
        model = Product
        fields = ['id', 'title', 'storeId', 'category',
                  'price', 'stock', 'condition', 'create_at']


class ProductImgserializer(serializers.ModelSerializer):
    class meat:
        model = Product
        fields = ['id', 'productId', 'url']


class Cartserializer(serializers.ModelSerializer):
    class meat:
        model = Cart
        fields = ['id', 'userId', 'quantity']


class CartItemserializer(serializers.ModelSerializer):
    class meat:
        model = CartItem
        fields = ['cartId', 'productId', 'quantity', 'create_at']


class FileUploadserializer(serializers.ModelSerializer):
    class meat:
        model = FileUpload
        fields = ['imgFile']


class Joinserializer(serializers.ModelSerializer):
    product_details = Productserializer(source='productId')

    class meat:
        model = CartItem
        fields = ['cartId', 'productId', 'quantity',
                  'product_details', 'create_at']
