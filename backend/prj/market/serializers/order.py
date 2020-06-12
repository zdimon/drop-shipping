from rest_framework import serializers
from market.models import Order, OrderProduct
from market.serializers.user_serializer import UserProfile
from market.serializers.product import ProductSerializer


class OrderProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderProduct
        fields = ['id', 'product', 'ammount']


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        out = []
        for i in OrderProduct.objects.filter(order=obj):
            out.append(OrderProductSerializer(i).data)
        return out

    class Meta:
        model = Order
        fields = ['id', 'consumer', 'created_at', 'status', 'products']
