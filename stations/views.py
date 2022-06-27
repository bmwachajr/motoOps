from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin,)
from rest_framework.response import Response
from rest_framework import status
from .models import Stations, StationSerializer


class StationsAPIView(GenericAPIView):
    queryset = Stations.objects.all()
    serializer_class = StationSerializer
    permission_classes = (AllowAny,)

    
    def post(self, request):
        """
        Method to handle post requests for creating a station
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        station:- the station data created by a user.
        endpoints.
        """
        serializer_class = StationSerializer
        station = request.data.get(
            'station', {}) if 'station' in request.data else request.data

        serializer = self.serializer_class(data=station)
        serializer.is_valid(raise_exception=True)
        new_station = serializer.save()

        resp_data = serializer_class(new_station).data

        return Response(resp_data, status=status.HTTP_201_CREATED)


    def get(self, request, *args, **kwargs):
        """
        Method to handle post requests for retrieving batteries
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        station:- the station data created by a user.
        endpoints.
        """
        self.serializer_class = StationSerializer
        return self.list(request, *args, **kwargs)

class StationAPIView(
        RetrieveModelMixin,
        DestroyModelMixin,
        UpdateModelMixin,
        GenericAPIView
    ):
    queryset = Stations.objects.all()
    serializer_class = StationSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        """
        Method to handle get requests for retrieving a station
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        station:- the station data retrieved by a user.
        endpoints.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Method to handle put requests for updating a station
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        station:- the station data updated by a user.
        endpoints.
        """        
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Method to handle delete requests for deleting a station
        """        
        return self.delete(request, *args, **kwargs)
