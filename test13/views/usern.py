from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from test13.models import UserN
from test13.serializers import UserNSerializer


class UserNViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserNSerializer
    queryset = UserN.objects.all()