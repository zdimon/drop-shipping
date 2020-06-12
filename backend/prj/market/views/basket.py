
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from market.models import Product, Order, OrderProduct
from market.serializers.basket import BasketRequestSerializer, BasketSubmitRequestSerializer
from market.serializers.product import ProductSerializer
from market.serializers.order import OrderSerializer

from market.models import Notification

from channels.layers import get_channel_layer
channel_layer = get_channel_layer()
from asgiref.sync import async_to_sync


class BasketInfoView(APIView):
    '''

    Получение информации о товарах в корзине.

    '''

    permission_classes = (AllowAny,)
    @swagger_auto_schema( 
        request_body = BasketRequestSerializer \
        )
    def post(self, request, format=None):
        out = []
        print(request.data['ids'])
        for it in request.data['ids']:
            out.append(ProductSerializer(Product.objects.get(pk=it)).data)
        return Response(out)

class BasketSubmitView(APIView):
    '''

    Submit basket.

    ___________________________

    '''

    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        request_body = BasketSubmitRequestSerializer, \
        responses={200: OrderSerializer} \
        )
    def post(self, request, format=None):
        o = Order()
        o.consumer = request.user.userprofile
        o.save()
        for item in request.data.get('products'):
            product = Product.objects.get(pk = item['product'])
            op = OrderProduct()
            op.product = product
            op.order = o
            op.ammount = item['ammount']
            op.save()

            noty = Notification()
            noty.product = product
            noty.consumer = request.user.userprofile
            noty.provider = product.user
            noty.save()
        
        async_to_sync(channel_layer.group_send)("notifications", {"type": "send_notify"})
            
        return Response(OrderSerializer(o).data)