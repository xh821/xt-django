from django.db import models
from django.forms import  ModelForm
from django import  forms
import django.utils.timezone as timezone
# Create your models here.

#入款单
class cwrkd(models.Model):
    time = models.DateTimeField(default=timezone.now)
    djbh = models.CharField(max_length=50)
    fkdw = models.CharField(max_length=30)
    jsr = models.CharField(max_length=20)
    bm  = models.CharField(max_length=20)
    fjsm = models.CharField(max_length=200)
    ps1 = models.CharField(max_length=200)
    ysje = models.IntegerField()
    yfje = models.IntegerField()
    zhbh = models.CharField(max_length=20)
    zhmc = models.CharField(max_length=20)
    jsfs = models.CharField(max_length=30)
    je = models.IntegerField()
    ps = models.CharField(max_length=100)
    zdr = models.CharField(max_length=20)

    def __str__(self):
        return  self.djbh

class cwrkdForm(forms.ModelForm):
    class Meta:
        model = cwrkd
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(cwrkdForm, self).__init__(*args, **kwargs)
#出款单
class cwckd(models.Model):
    time = models.DateTimeField(default=timezone.now)
    djbh = models.CharField(max_length=50)
    fkdw = models.CharField(max_length=30)
    jsr = models.CharField(max_length=20)
    bm  = models.CharField(max_length=20)
    fjsm = models.CharField(max_length=200)
    ps1 = models.CharField(max_length=200)
    ysje = models.IntegerField()
    yfje = models.IntegerField()
    zhbh = models.CharField(max_length=20)
    zhmc = models.CharField(max_length=20)
    jsfs = models.CharField(max_length=30)
    je = models.IntegerField()
    ps = models.CharField(max_length=100)
    zdr = models.CharField(max_length=20)

    def __str__(self):
        return  self.djbh

class cwckdForm(forms.ModelForm):
    class Meta:
        model = cwrkd
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(cwckdForm, self).__init__(*args, **kwargs)
#计算利润
class jslr(models.Model):
    qssj = models.DateTimeField(default=timezone.now)
    jssj = models.DateTimeField(default=timezone.now)
    # lrzje = models.IntegerField()

    def __str__(self):
        return self.qssj


class jslrForm(forms.ModelForm):
    class Meta:
        model = jslr
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(jslrForm, self).__init__(*args, **kwargs)

