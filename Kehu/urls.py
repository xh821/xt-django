# -*- coding: UTF-8 -*-
from django.urls import path
from  Kehu import  views


app_name = 'Kehu'
urlpatterns = [
    path('khxx',views.khxx1,name = 'khxx'),
    path('khgl',views.khgl,name = 'khgl')

]