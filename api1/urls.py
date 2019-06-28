from django.urls import path

from .views import AddAdminUser

urlpatterns = [
    
    path('addAdminUser/', AddAdminUser, name='AddAdminUser'),
    
]
