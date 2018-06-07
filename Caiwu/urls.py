# -*- coding: UTF-8 -*-
from django.urls import path
from  Caiwu import  views

app_name = 'Caiwu'
urlpatterns = [

    path('cw-ckd',views.addckd,name = 'cw-ckd'),
    path('cw-rkd',views.addrkd,name = 'cw-rkd'),
    path('cw-jslr',views.jslr,name = 'cw-jslr'),



]