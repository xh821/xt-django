from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponseRedirect
from django import forms
from Cangk.models import *
from Cangk import models
from django.contrib.auth.decorators import login_required

#主页---重定向

#入库单 rkd.html
@login_required(redirect_field_name='',login_url='/login')
def addrkd(request):
    if request.method =='POST':
        form = rkdForm(request.POST)
        if form.is_valid():
            lzsj = form.cleaned_data['lzsj']
            djbh = form.cleaned_data['djbh']
            ghdw = form.cleaned_data['ghdw']
            jsr = form.cleaned_data['jsr']
            bm = form.cleaned_data['bm']
            rkck =form.cleaned_data['rkck']
            ps1 = form.cleaned_data['ps1']

            spbh =form.cleaned_data['spbh']
            spmc = form.cleaned_data['spmc']
            dw = form.cleaned_data['dw']
            sl = form.cleaned_data['sl']
            rkdj = form.cleaned_data['rkdj']
            rkje = form.cleaned_data['rkje']
            ps2 = form.cleaned_data['ps2']
            RKD = rkd(
                lzsj=lzsj,djbh=djbh,ghdw=ghdw,jsr=jsr,bm =bm,rkck=rkck,
                ps1 =ps1,spbh =spbh,spmc =spmc,dw=dw,sl=sl,rkdj =rkdj,
                rkje =rkje,ps2 =ps2,
            )
            RKD.save()
            return HttpResponseRedirect('index')
    else:
        form = rkdForm()
    return render(request,'ck-rkd.html',{'form':form})

#出库单 ckd.html
@login_required(redirect_field_name='',login_url='/login')
def addckd(request):
    if request.method == 'POST':
        form = ckdForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['time']
            djbh = form.cleaned_data['djbh']
            mddw = form.cleaned_data['mddw']
            jsr = form.cleaned_data['jsr']
            bm = form.cleaned_data['bm']
            ckck = form.cleaned_data['ckck']
            ps1 = form.cleaned_data['ps1']
            spid = form.cleaned_data['spid']
            spname = form.cleaned_data['spname']
            danwei = form.cleaned_data['danwei']
            ck = form.cleaned_data['ck']
            num = form.cleaned_data['num']
            ckdj = form.cleaned_data['ckdj']
            ckje = form.cleaned_data['ckje']
            ps2 = form.cleaned_data['ps2']
            Ckd = ckd(time=time,djbh=djbh,mddw=mddw,jsr=jsr,bm=bm,
                      ckck=ckck,ps1=ps1,spid=spid,spname=spname,
                      danwei=danwei,ck=ck,num=num,ckdj=ckdj,ckje=ckje,ps2=ps2,
                      )
            Ckd.save()
            return HttpResponseRedirect('ck-kffp')
    else:
        form = ckdForm()
    return render(request,'ck-ckd.html',{'form':form})


# 库房管理 kfgl.html
@login_required(redirect_field_name='',login_url='/login')
def kfgladd(request):
  return render(request, 'ck-ckgl.html', )

#增加仓库  ck-addck.html
@login_required(redirect_field_name='',login_url='/login')
def addck(request):
    if request.method == 'POST':
        form = ckaddForm(request.POST)
        if form.is_valid():
            ckID = form.cleaned_data['ckID']
            ckname = form.cleaned_data['ckname']
            ckperson = form.cleaned_data['ckperson']
            dz = form.cleaned_data['dz']
            ps1 = form.cleaned_data['ps1']
            person = form.cleaned_data['person']
            tel = form.cleaned_data['tel']
            ps2 = form.cleaned_data['ps2']
            CKADD = ck(ckID=ckID,ckname=ckname,ckperson=ckperson,dz =dz,
                   ps1 = ps1,person=person,tel=tel,ps2=ps2,
                   )
            CKADD.save()
            return HttpResponseRedirect('ck-kffp')
    else:
        form = ckaddForm()
    return render(request,'ck-addck.html',{'form':form})

# 库房分配总信息  kffp.html
@login_required(redirect_field_name='',login_url='/login')
def kffpadd(request):
      spxx = rkd.objects.all()
      return render(request,"ck-kffp.html",locals())














