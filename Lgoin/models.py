from django.db import models
from django.forms import ModelForm
from django import  forms
import django.utils.timezone as timezone
from django.contrib.auth.models import User
from  django.db.models.signals import post_save

# BUM =(
#         (0,'销售部'),#负责客户 订单
#         (1,'财务部'),#负责财务
#         (2,'人事部'),#负责员工信息
#         (3,'仓管部'),# 负责仓库 产品
#         (4,'管理部'),
#     )
# class UserProfile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     bum = models.IntegerField(choices=BUM,default=0)
#
# def create_user_profile(sender,instance,created,**kwargs):
#     if created:
#         profile,created =UserProfile.objects.get_or_create(user=instance)
#
# post_save.connect(create_user_profile,sender=User)
# Create your models here.


#
# class User(models.Model):
#     BUM =(
#         (0,'销售部'),#负责客户 订单
#         (1,'财务部'),#负责财务
#         (2,'人事部'),#负责员工信息
#         (3,'仓管部'),# 负责仓库 产品
#         (4,'管理部'),
#     )
#     username = models.CharField(max_length=30)
#     userpwd = models.CharField(max_length=50)
#     zctime = models.DateField(blank=True,null= True,default=timezone.now)
#     bum = models.IntegerField(choices=BUM,default=0)
#     def __str__(self):
#         return  self.username
#
# class USERRForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = "__all__"
#     def __init__(self, *args, **kwargs):
#         super(userForm, self).__init__(*args, **kwargs)
