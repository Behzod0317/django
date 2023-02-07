
from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [

    path('', MenuView.as_view(), name='menu'),
    #path('item/<int:item_id>/', item, name='item'),
]
