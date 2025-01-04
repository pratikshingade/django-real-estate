from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        exclude = ['pkid', 'created_at', 'updated_at']

        def get_user(self, obj):
            return obj.user.username


class PropertyCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        exclude = ['pkid', 'updated_at']


class PropertyViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        exclude = ['pkid', 'updated_at']
