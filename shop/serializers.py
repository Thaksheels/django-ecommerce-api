from rest_framework import serializers
from shop.models import Category,Product,Cart,Shipment,Payment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
    
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shipment
        fields="__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields="__all__"