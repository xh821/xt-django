# -*- coding: UTF-8 -*-
from django.urls import path
from  Dindan import  views



app_name = 'Dindan'
urlpatterns = [
    path('dd-zjdd',views.zjdd1,name = 'dd-zjdd'),
    path('dd-ddgl',views.ddgl,name = 'dd-ddgl'),
    path('dd-shdd',views.shdd,name = 'dd-shdd'),

]