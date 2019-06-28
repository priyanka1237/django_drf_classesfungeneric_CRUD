from django.contrib.auth.models import User

from rest_framework import serializers
from api1.models import OtherUserDetails, Item


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

class OtherUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OtherUserDetails
        fields = ('id', 'dob', 'socialId', 'role', 'profile_pic', 'gender', 'user_auth', 'address', 'idType', 'idNumber', 'status', 'designationName', 'onOffNotification')

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'description', 'status')