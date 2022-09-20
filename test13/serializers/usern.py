from rest_framework import serializers

from test13.models import UserN


class UserNSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserN
        fields = ('__all__')