from django.db import models
from django.forms import  ModelForm
from django import  forms
import django.utils.timezone as timezone

# Create your models here.
class addsp(models.Model):
    spmc = models.CharField(max_length=20)
    spbh = models.CharField(max_length=20)
    pp = models.CharField(max_length=20)
    gg = models.CharField(max_length=120)
    xh = models.CharField(max_length=50)
    zl = models.IntegerField()
    scsj = models.DateTimeField(default=timezone.now)
    bzq = models.DateTimeField(default=timezone.now)
    bxsj = models.CharField(max_length=20)
    ghxx = models.CharField(max_length=200)
    ckcb = models.IntegerField()
    ps = models.CharField(max_length=100)
    dwmc = models.CharField(max_length=100)
    dwdm = models.CharField(max_length=50)
    tm = models.IntegerField()
    lsj = models.IntegerField()
    y1 = models.IntegerField()
    y2 = models.IntegerField()
    y3 = models.IntegerField()
    def __str__(self):
        return  self.spmc

class addspForm(forms.ModelForm):
    class Meta:
        model = addsp
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(addspForm, self).__init__(*args, **kwargs)

class addspimg(models.Model):
    STATUS_SIZES = (
        (0,'进行中'),
        (1,'已完成'),
    )
    imgf = models.ImageField(upload_to='upload')
    name1 = models.CharField(max_length=10, default='前面')
    imgb = models.ImageField(upload_to='upload')
    name2 = models.CharField(max_length=10, default='后面')
    imgl = models.ImageField(upload_to='upload')
    name3 = models.CharField(max_length=10, default='左面')
    imgr = models.ImageField(upload_to='upload')
    name4 = models.CharField(max_length=10, default='右面')
    imgu = models.ImageField(upload_to='upload')
    name5 = models.CharField(max_length=10, default='上面')
    imgd = models.ImageField(upload_to='upload')
    name6 = models.CharField(max_length=10, default='底面')
    status = models.IntegerField('状态',default=0,choices=STATUS_SIZES)

    def __str__(self):
        return self.name1

class addspimgForm(forms.ModelForm):
    class Meta:
        model = addspimg
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(addspimgForm, self).__init__(*args, **kwargs)




