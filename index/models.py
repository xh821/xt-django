from django.db import models
from django.forms import ModelForm
from  django import forms

# Create your models here.


class LYinfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    text = models.TextField()
    def __str__(self):
        return  self.phone

class LYinfoForm(forms.ModelForm):
    class Meta:
        model = LYinfo
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(LYinfoForm, self).__init__(*args, **kwargs)
