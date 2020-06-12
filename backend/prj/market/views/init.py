from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from market.serializers.init_serializer import InitSerializer
from drf_yasg.utils import swagger_auto_schema
from market.serializers.user_serializer import UserProfileSerializer

class InitView(APIView):
    '''
    
    Проверка на авторизованность.

    _______________________


    '''
    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: InitSerializer} )
    def get(self, request, format=None):
        try:
            token = Token.objects.get(user=request.user)
            resp = InitSerializer({"token": token.key, "user": UserProfileSerializer(request.user.userprofile).data}).data
        except Exception as e:
             resp = {"status": 1, "message": str(e)}
        return Response(resp)