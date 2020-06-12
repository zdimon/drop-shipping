from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from market.models import Notification
from market.serializers.notification import NotificationSerializer
from rest_framework.permissions import IsAuthenticated

class NotifyListView(ListModelMixin,GenericAPIView):
    queryset = Notification.objects.order_by('-id')
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return Notification.objects.filter(provider=self.request.user.userprofile)

    