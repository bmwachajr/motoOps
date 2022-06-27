from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin,)
from rest_framework.response import Response
from rest_framework import status
from .models import Batteries, BatterySerializer


class BatteriesAPIView(ListModelMixin, GenericAPIView):
    queryset = Batteries.objects.all()
    serializer_class = BatterySerializer
    permission_classes = (AllowAny,)

    
    def post(self, request):
        """
        Method to handle post requests for creating a battery
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        battery:- the battery data created by a user.
        endpoints.
        """
        serializer_class = BatterySerializer
        battery = request.data.get(
            'battery', {}) if 'battery' in request.data else request.data

        serializer = self.serializer_class(data=battery)
        serializer.is_valid(raise_exception=True)
        new_battery = serializer.save()

        resp_data = serializer_class(new_battery).data

        return Response(resp_data, status=status.HTTP_201_CREATED)


    def get(self, request, *args, **kwargs):
        """
        Method to handle post requests for retrieving batteries
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        battery:- the battery data created by a user.
        endpoints.
        """
        self.serializer_class = BatterySerializer
        return self.list(request, *args, **kwargs)

class BatteryAPIView(
        RetrieveModelMixin,
        DestroyModelMixin,
        UpdateModelMixin,
        GenericAPIView
    ):
    queryset = Batteries.objects.all()
    serializer_class = BatterySerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        """
        Method to handle get requests for retrieving a battery
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        battery:- the battery data retrieved by a user.
        endpoints.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Method to handle put requests for updating a battery
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        battery:- the battery data updated by a user.
        endpoints.
        """        
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Method to handle delete requests for deleting a battery
        """        
        return self.delete(request, *args, **kwargs)
