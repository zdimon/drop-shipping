from rest_framework import serializers
from market.serializers.product import ProductSerializer


class BasketRequestSerializer(serializers.Serializer):
    ids = serializers.ListField(
                child=serializers.IntegerField(min_value=1) \
            )

class BasketItemSerializer(serializers.Serializer):
    product = serializers.IntegerField(min_value=1)
    ammount = serializers.IntegerField(min_value=1)

class BasketSubmitRequestSerializer(serializers.Serializer):
    products = serializers.ListField(
                child=BasketItemSerializer() \
            )