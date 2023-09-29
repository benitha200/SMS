from rest_framework import serializers
from .models import Product, Stock, StockIn, StockOut, Payment_confirmation
from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class StockInSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockIn
        fields = '__all__'


class StockOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockOut
        fields = '__all__'


class PaymentConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_confirmation
        fields = '__all__'
