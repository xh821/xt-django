from django.shortcuts import render,HttpResponseRedirect
from  index.models import *
from Caiwu.models import cwrkd
from  Dindan.models import zjdd
from Cangk.models import ckd
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(redirect_field_name='',login_url='/login')
def index(request):
    #登录信息
    lginfo = User.objects.order_by('-id')[:6]
    #成交金额
    CW = cwrkd.objects.all()
    cjje = 0
    for id in CW:
        cjje = cjje + id.je
    #订单数
    DD = zjdd.objects.order_by('id')[:1]
    ddzs = 1
    for id in DD:
        ddzs = id.id

     #销售排行
    CKD = ckd.objects.order_by('num')[:5]
    #留言
    LY = LYinfo.objects.order_by('-id')[:1]
    for id in LY:
        lys = id.id
    return render(request,'index.html',locals())

@login_required(redirect_field_name='',login_url='/login')
def Liuyan(request):
    if request.method =='POST':
        form = LYinfoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email =form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            text =  form.cleaned_data['text']
            ZJLY = LYinfo(
                name =name,email =email,phone =phone,text = text,
            )
            ZJLY.save()
            return HttpResponseRedirect('index')
    else:
        form = LYinfoForm()
    return render(request,'Liuyan.html',{'form':form})
