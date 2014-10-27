from rest_framework import status
from rest_framework.decorators import api_view
from services.models import DepartureTime
from services.serializers import DepartureTimeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.application import getDepartureTime

# Create your views here.
class DepartureTimeList(APIView):
    """
    List all DepartureTime, or create a new DepartureTime.
    """
    def get(self, request, format=None):

        # hardcoded to getDepartureTime 10
        if 'u1' in request.QUERY_PARAMS:
            print (request.QUERY_PARAMS['u1'])
        if 'u2' in request.QUERY_PARAMS:
            print (request.QUERY_PARAMS['u2'])

        time = getDepartureTime(10)

        # time = (DepartureTime(stopCode=12345, stopName="Milbrae"), DepartureTime(stopCode=1234, stopName="Daly City"))
        serializer = DepartureTimeSerializer(time, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartureTimeSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)