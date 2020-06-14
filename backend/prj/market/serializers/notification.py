from rest_framework import serializers
from market.models import Notification
from market.serializers.user_serializer import UserProfileSerializer
from market.serializers.product import ProductSerializer

class NotificationSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Notification
        fields = ['id', 'provider', 'product', 'phone', 'created_at', 'ammount'] 