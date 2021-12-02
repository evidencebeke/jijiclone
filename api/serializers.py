from rest_framework import serializers
from .models import Buyer, Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'location', 'imgUrl', 'isSold', 'seller')
        model = Product


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'phoneNumber', 'email', 'product' )
        model = Buyer