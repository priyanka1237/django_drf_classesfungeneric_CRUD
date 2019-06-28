'''
Created on 28-Jun-2019

@author: netset
'''
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api1.models import OtherUserDetails, Item
from api1.serializers import ItemSerializer


class ItemViews(APIView):
    """
    List all items, or create a new item.
    """
    def get(self, request, format=None):
        items = Item.objects.all()
        itemsSerializer = ItemSerializer(items, many=True)
        return Response(itemsSerializer.data)
    
    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    