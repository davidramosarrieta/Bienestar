# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from src.api.serializers.user_serializer import CitySerializer
from src.users.models import City


class ApiUserDetailView(APIView):

    @api_view(['GET'])
    def user_cities(request):
        """
        Return group list registered in the system.
        """
        cities = City.objects.all().order_by('id')
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
