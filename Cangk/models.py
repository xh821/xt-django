from django.db import models
from django.forms import ModelForm
from django import  forms
import  django.utils.timezone as timezone


#入库单
RKCK = (
         (1,'Chengdu'),(2,'Deyang'),(3,'Mianyang'),(4,'Xian'),
    )
class rkd(models.Model):

    lzsj = models.DateTimeField(default=timezone.now)
    djbh =models.CharField(max_length=30)
    ghdw = models.CharField(max_length=20)
    jsr = models.CharField(max_length=20)
    bm = models.CharField(max_length=100)
    rkck = models.CharField(max_length=20)
    ps1 = models.CharField(max_length=50)

    spbh = models.CharField(max_length=100)
    spmc = models.CharField(max_length=100)
    dw = models.CharField(max_length=10)
    sl = models.IntegerField()
    rkdj = models.IntegerField()
    rkje = models.IntegerField()
    ps2 = models.CharField(max_length=100)

    def __str__(self):
        return self.djbh

class rkdForm(ModelForm):
    class Meta:
        model = rkd
        fields = "__all__"
    def __init__(self,*args,**kwargs):
        super(rkdForm,self).__init__(*args,**kwargs)
  #仓库信息表
class ck(models.Model):
        ckID = models.IntegerField()
        ckname = models.CharField(max_length=30)
        ckperson = models.CharField(max_length=10)
        dz = models.CharField(max_length=200)
        ps1 = models.CharField(max_length=100)
        person = models.CharField(max_length=10)
        tel = models.IntegerField()
        ps2 = models.CharField(max_length=100)

        def __str__(self):
            return self.ckID

class ckaddForm(forms.ModelForm):
        class Meta:
            model = ck
            fields = "__all__"

        def __init__(self, *args, **kwargs):
             super(ckaddForm, self).__init__(*args, **kwargs)

   #出库单
class ckd(models.Model):

        time = models.DateTimeField(default=timezone.now)
        djbh = models.IntegerField()
        mddw = models.CharField(max_length=150)
        jsr = models.CharField(max_length=10)
        bm = models.CharField(max_length=20)
        ckck = models.CharField(max_length=100)
        ps1 = models.CharField(max_length=100)
        spid = models.IntegerField()
        spname = models.CharField(max_length=50)
        danwei = models.CharField(max_length=10)
        ck = models.CharField(max_length=100)
        num = models.IntegerField()
        ckdj = models.IntegerField()
        ckje = models.IntegerField()
        ps2 = models.CharField(max_length=100)

        def __str__(self):
            return self.djbh

class ckdForm(forms.ModelForm):
        class Meta:
            model = ckd
            fields = "__all__"

        def __init__(self, *args, **kwargs):
             super(ckdForm, self).__init__(*args, **kwargs)


#库房分配


class kffp(models.Model):
    di = models.IntegerField()
    spbh = models.IntegerField()
    spmc = models.CharField(max_length=20)
    ck = models.IntegerField(choices=RKCK, default=1)
    sl = models.IntegerField()
    je = models.IntegerField()

    def __str__(self):
        return self.di

class kffpForm(forms.ModelForm):
    class Meta:
        model = kffp
        fields = "__all__"
    def __init__(self,*args,**kwargs):
        super(kffpForm,self).__init__(*args,**kwargs)











