from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OtherUserDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    dob = models.DateField(blank=True, null=True)
    socialId = models.CharField(max_length=255, default="")
    role = models.IntegerField()
    profile_pic = models.CharField(max_length=255, default="")
    gender = models.CharField(max_length=1, default="m")
    user_auth = models.ForeignKey(User, null="True", on_delete=models.CASCADE)
    address = models.CharField(max_length=255, default="")
    idType = models.CharField(max_length=255, default="")
    idNumber = models.CharField(max_length=255, default="")
    status = models.IntegerField(default=1)
    designationName = models.CharField(max_length=255, default="")
    onOffNotification = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'otheruserdetails'
        
class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")
    price = models.FloatField(default=1)
    description = models.TextField(max_length=500, null=True)
    status = models.IntegerField(default=1)
    
    class Meta:
        db_table = 'item'
# Create your models here.
