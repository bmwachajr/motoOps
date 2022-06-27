from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin,)
from rest_framework.response import Response
from rest_framework import status
from .models import PostSwapSerializer, Swaps, SwapSerializer


class SwapsAPIView(ListModelMixin, GenericAPIView):
    queryset = Swaps.objects.all()
    serializer_class = PostSwapSerializer
    permission_classes = (AllowAny,)

    
    def post(self, request):
        """
        Method to handle post requests for creating a battery swap
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        battery swap:- the battery swap data created by a user.
        endpoints.
        """
        serializer_class = PostSwapSerializer
        swap = request.data.get(
            'swap', {}) if 'swap' in request.data else request.data

        serializer = serializer_class(data=swap)
        serializer.is_valid(raise_exception=True)
        new_swap = serializer.save()

        resp_data = serializer_class(new_swap).data

        return Response(resp_data, status=status.HTTP_201_CREATED)


    def get(self, request, *args, **kwargs):
        """
        Method to handle post requests for retrieving batteries
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        battery swap:- the battery swap data created by a user.
        endpoints.
        """
        self.serializer_class = SwapSerializer
        return self.list(request, *args, **kwargs)

class SwapAPIView(
        RetrieveModelMixin,
        DestroyModelMixin,
        UpdateModelMixin,
        GenericAPIView
    ):
    queryset = Swaps.objects.all()
    serializer_class = SwapSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        """
        Method to handle get requests for retrieving a battery swap
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        battery swap:- the battery swap data retrieved by a user.
        endpoints.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Method to handle put requests for updating a battery swap
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        battery swap:- the battery swap data updated by a user.
        endpoints.
        """        
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Method to handle delete requests for deleting a battery swap
        """        
        return self.delete(request, *args, **kwargs)
