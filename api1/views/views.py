from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from api1.models import OtherUserDetails, Item
from api1.serializers import ItemSerializer

# Create your views here.


@api_view(['POST'])
def AddAdminUser(request):
    try:
        with transaction.atomic():
            # serializer.save()
            username = request.data['username']
            password = request.data['password']
            email = request.data['email']
            firstname = request.data['firstname']
            lastname = request.data['lastname']
            
            address = request.data['address']
            idType = request.data['idType']
            idNumber = request.data['idNumber']
            
            user = User.objects.create(username=username,
                                 email=email,
                                 first_name=firstname,
                                 last_name=lastname,
                                 password=make_password(password),
                                 is_superuser=0,
                                 is_staff=0,
                                 is_active=1,
                                date_joined=timezone.now())
            if user is not None:
                g = Group.objects.get(name='Admin')
                g.user_set.add(user)
                otherUserDetails = OtherUserDetails.objects.create(address=address,
                                 idType=idType,
                                 idNumber=idNumber,
                                 user_auth_id=user.id,
                                 role=1
                                 );
                if otherUserDetails is not None:
                    return Response({"message" : "Done", "status" : "1", "object" : {"id" : otherUserDetails.id, "firstname" : user.first_name, "lastname" : user.last_name, "username" : user.username, "email" : user.email, "address" : otherUserDetails.address}}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message" : "Sorry Something Went Wrong", "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({"message" : "Sorry Something Went Wrong", "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
            
    except Exception as e:
        print(e)
        return Response({"message" : "Sorry Something Went Wrong", "status" : "0"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
@api_view(['GET', 'POST'])
def item_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
 
@api_view(['GET', 'PUT', 'DELETE'])
def item_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)