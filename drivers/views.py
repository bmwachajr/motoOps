from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin,)
from rest_framework.response import Response
from rest_framework import status
from .models import Drivers, DriverSerializer


class DriversAPIView(GenericAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (AllowAny,)

    
    def post(self, request):
        """
        Method to handle post requests for creating a driver
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        driver:- the driver data created by a user.
        endpoints.
        """
        serializer_class = DriverSerializer
        driver = request.data.get(
            'driver', {}) if 'driver' in request.data else request.data

        serializer = self.serializer_class(data=driver)
        serializer.is_valid(raise_exception=True)
        new_driver = serializer.save()

        resp_data = serializer_class(new_driver).data

        return Response(resp_data, status=status.HTTP_201_CREATED)


    def get(self, request, *args, **kwargs):
        """
        Method to handle post requests for retrieving batteries
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        driver:- the driver data created by a user.
        endpoints.
        """
        self.serializer_class = DriverSerializer
        return self.list(request, *args, **kwargs)

class DriverAPIView(
        RetrieveModelMixin,
        DestroyModelMixin,
        UpdateModelMixin,
        GenericAPIView
    ):
    queryset = Drivers.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        """
        Method to handle get requests for retrieving a driver
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        driver:- the driver data retrieved by a user.
        endpoints.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Method to handle put requests for updating a driver
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        driver:- the driver data updated by a user.
        endpoints.
        """        
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Method to handle delete requests for deleting a driver
        """        
        return self.delete(request, *args, **kwargs)
