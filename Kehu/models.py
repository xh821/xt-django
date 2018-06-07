from django.db import models
from django import forms
# Create your models here.

class khxx(models.Model):
    DJ = (
        (0,'普通会员'),(1,'VIP会员')
         )
    khbh = models.IntegerField()
    khmc = models.CharField(max_length=20)
    khlx = models.CharField(max_length=10)
    khdj = models.IntegerField()
    khyh = models.CharField(max_length=20)
    yhzh = models.IntegerField()
    xsry = models.CharField(max_length=20)
    lxr = models.CharField(max_length=10)
    tel = models.IntegerField()
    tel2 = models.IntegerField()
    dz = models.CharField(max_length=200)
    sfzh = models.CharField(max_length=50)

    def __str__(self):
        return self.khbh

class khxxForm(forms.ModelForm):
    class Meta:
        model = khxx
        fields ='__all__'
    def __init__(self, *args, **kwargs):
        super(khxxForm, self).__init__(*args, **kwargs)

