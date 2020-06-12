from rest_framework import serializers
from market.models import Product

from market.serializers.category import CategorySerializer
from market.serializers.subcategory import SubCategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'get_small_image_url', 'price'] 


class AddProductRequestSerializer(serializers.Serializer):
    cat = serializers.IntegerField(min_value=1)
    subcat = serializers.IntegerField(min_value=1)
    name = serializers.CharField()
    image = serializers.FileField(allow_empty_file=True, required=False)
    imager_base64 = serializers.CharField(required=False)

