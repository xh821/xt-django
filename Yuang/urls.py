# -*- coding: UTF-8 -*-
from django.urls import path
from  Yuang import  views
app_name = 'Yuang'
urlpatterns = [
    path('ygxxadd',views.ygxxadd,name = 'ygxxadd'),
    path('ygxxgl',views.ygxxgl,name = 'ygxxgl'),

]