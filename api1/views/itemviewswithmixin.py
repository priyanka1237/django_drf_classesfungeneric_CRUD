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
from rest_framework import mixins
from rest_framework import generics



class ItemViewsWithMixin(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    