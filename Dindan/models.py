from django.db import models
from django.forms import ModelForm
from  django import forms
import django.utils.timezone as timezone

# Create your models here.
#增加订单
class zjdd(models.Model):
    SHZT=(
        (1,'已审核'),
        (0,'未审核'),
    )
    time = models.DateTimeField(default=timezone.now)
    djbh = models.CharField(max_length=20)
    dhsj = models.DateTimeField(default=timezone.now)
    dhdw = models.CharField(max_length=40)
    spbh = models.CharField(max_length=50)
    spmc = models.CharField(max_length=30)
    sl = models.IntegerField()
    dj = models.IntegerField()
    je = models.IntegerField()
    zdr = models.CharField(max_length=20)
    sh = models.IntegerField('审核状态',choices=SHZT,default=0)

    def __str__(self):
        return  self.djbh

class zjddForm(forms.ModelForm):
    class Meta:
        model = zjdd
        fields ='__all__'
    def __init__(self, *args, **kwargs):
        super(zjddForm, self).__init__(*args, **kwargs)


