from django_filters import FilterSet, NumberFilter, CharFilter
from market.models import Product

class ProductFilter(FilterSet):
    category = NumberFilter()
    subcategory = NumberFilter()
    searchkey = CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Product
        fields = ['category', 'searchkey', 'subcategory']