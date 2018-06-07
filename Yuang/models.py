from django.db import models
from django import forms
import django.utils.timezone as timezone
# Create your models here.
class ygxx(models.Model):
    BM=(
        (0,'销售部'),#负责客户 订单
        (1,'财务部'),#负责财务
        (2,'人事部'),#负责员工信息
        (3,'仓管部'),# 负责仓库 产品
    )
    bh = models.CharField(max_length=15)
    name = models.CharField(max_length=10)
    tel  = models.CharField(max_length=11)
    bum = models.IntegerField(choices=BM,default=0)
    sfzh = models.CharField(max_length=100)
    gzkh = models.CharField(max_length=100)
    rzsj = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.bh

class ygxxForm(forms.ModelForm):
    class Meta:
        model = ygxx
        fields ='__all__'
    def __init__(self, *args, **kwargs):
        super(ygxxForm, self).__init__(*args, **kwargs)

