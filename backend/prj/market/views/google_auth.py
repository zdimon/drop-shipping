from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User

from drf_yasg.utils import swagger_auto_schema
from market.serializers.google_auth import GoogleAuthRequestSerializer
from rest_framework.authtoken.models import Token

from market.models import UserProfile
import requests
from prj.settings import BASE_DIR
from django.core.files import File

from market.serializers.user_serializer import UserProfileSerializer

class GoogleView(APIView):
    '''
    Авторизация через гугл.

    '''
    permission_classes = (AllowAny,)
    
    @swagger_auto_schema( 
        request_body = GoogleAuthRequestSerializer \
        )
    def post(self, request, format=None):
        print(request.data)
        try:
            p = UserProfile.objects.get(username=request.data['email'])
            token = Token.objects.get(user=p)
        except:
            
            p = UserProfile()
            p.name = request.data['firstName']
            p.username = request.data['email']
            p.is_active = True
            p.set_password('123')
            p.save()
            token = Token.objects.create(user=p)
            # тянем картинку и сохраняем во временный файл
            r = requests.get(request.data['photoUrl'], stream=True)
            if r.status_code == 200:
                filename = '%s/tmp.jpg' % BASE_DIR
                with open(filename, 'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
                with open(filename, 'rb') as image:
                    p.image.save('%s.jpeg'% p.id, File(image), save=True)

        return Response({
            'token': token.key,
            'agent': request.META['HTTP_USER_AGENT'],
            'user': UserProfileSerializer(p).data
        })