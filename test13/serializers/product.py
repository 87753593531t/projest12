from rest_framework import serializers

from test13.models import Product, UserN
from .usern import UserNSerializer


class ProductsSerializer(serializers.ModelSerializer):
    usern = UserNSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'quality',
            'usern'
        )

    def validate(self, attrs):

        return attrs

    def create(self, validated_data):
        user_data = validated_data['usern']
        old_user = UserN.objects.filter(name=user_data['name'])
        old_user = old_user.filter(surname=user_data['surname'])
        if old_user.exists():
            validated_data['usern'] = old_user.first()
        else:
            user = UserNSerializer(data=user_data)
            user.is_valid(raise_exception=True)
            user.save()
            validated_data['usern'] = user.instance
        return super().create(validated_data)
