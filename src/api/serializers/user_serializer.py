from rest_framework import serializers

from src.users.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        lookup_field = 'id'
        fields = ('id', 'name', 'latitude', 'longitude', 'group')
