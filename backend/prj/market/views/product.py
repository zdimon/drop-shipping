from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from market.models import Product
from rest_framework import serializers
from market.views.category import CategorySerializer, SubCategorySerializer

from market.filters import ProductFilter

from market.serializers.product import ProductSerializer

class ProductListView(ListModelMixin,GenericAPIView):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
