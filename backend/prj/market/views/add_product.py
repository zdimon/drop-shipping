from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from django.core.files.base import ContentFile
import base64

from market.serializers.product import ProductSerializer, AddProductRequestSerializer
from market.models import Product, Category, SubCategory

class AddProductView(APIView):
    """
    Adding a new product.

    _____________________

    """
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema( 
        request_body = AddProductRequestSerializer, \
        responses={200: ProductSerializer} \
        )
    def post(self, request, format=None):

        #cat = Category.objects.get(pk=request.data.get('cat'))
        #subcat = SubCategory.objects.get(pk=request.data.get('subcat'))
        p = Product()
        #p.category = cat
        p.price = request.data.get('price')
        p.user = request.user.userprofile
        #p.subcategory = subcat
        p.name = request.data.get('name')
        

        if "image" in request.data:
            p.image = (request.data['image'])

        if "image_base64" in request.data:
            try:
                format, imgstr = request.data.get('image_base64').split(';base64,')
                ext = format.split('/')[-1]
                data = ContentFile(base64.b64decode(imgstr))
                file_name = '%s_user.%s' % (p.id,ext) 
                p.image.save(file_name, data, save=True)
            except:
                pass

        p.save()

        return Response(ProductSerializer(p).data)