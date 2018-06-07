# -*- coding: UTF-8 -*-
from django.urls import path
from  Cangk import  views


app_name = 'Cangk'
urlpatterns = [

        path('ck-rkd',views.addrkd,name='ck-rkd'),
        path('ck-ckd',views.addckd,name='ck-ckd'),
        path('ck-kffp',views.kffpadd,name='ck-kffp'),
        path('ck-kfgl',views.kfgladd,name='ck-kfgl'),
        path('ck-addck',views.addck,name='ck-addck'),

]