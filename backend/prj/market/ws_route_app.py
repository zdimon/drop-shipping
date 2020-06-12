from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from market.consumer import MarketConsumer
from django.urls import re_path

application = ProtocolTypeRouter({
    
    'websocket': AuthMiddlewareStack(
        URLRouter( [
            re_path(r'market$', MarketConsumer),
         ]
        )
    ),


})