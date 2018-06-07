# -*- coding: UTF-8 -*-
from django.urls import path
from  Chanpin import  views


app_name = 'Chanpin'
urlpatterns = [
      path('addsp', views.addsp1,name='addsp'),
      path('addspimg',views.addspimg,name='addspimg'),
      path('cp-cpgl',views.cpgl,name ='cp-cpgl'),

]