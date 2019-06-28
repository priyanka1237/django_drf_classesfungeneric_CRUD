'''
Created on 28-Jun-2019

@author: netset
'''

from rest_framework import generics
from api1.models import Item
from api1.serializers import ItemSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer