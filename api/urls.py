"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api1 import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api1',include('api1.urls')),
    path('addAdminUser/',api_views.AddAdminUser, name='AddAdminUser'),
    path('items/', api_views.ItemViews.as_view()),
    path('items/<int:pk>/', api_views.ItemViewsWithArg.as_view()),
    
    
    
    
    
    
    path('items2/', api_views.item_list),
    path('items2/<int:pk>', api_views.item_detail),
    
    
    
    path('items3/', api_views.ItemViewsWithMixin.as_view()),
    path('items3/<int:pk>/', api_views.ItemViewsWithArgAndMixin.as_view()),
    
    
    
    
    
    
    path('items4/', api_views.ItemList.as_view()),
    path('items4/<int:pk>/', api_views.ItemDetail.as_view()),
]
