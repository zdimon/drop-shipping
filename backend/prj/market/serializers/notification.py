from rest_framework import serializers
from market.models import Notification
from market.serializers.user_serializer import UserProfileSerializer
from market.serializers.product import ProductSerializer

class NotificationSerializer(serializers.ModelSerializer):
    consumer = UserProfileSerializer() 
    product = ProductSerializer()

    class Meta:
        model = Notification
        fields = ['id', 'consumer', 'provider', 'product', 'created_at'] 