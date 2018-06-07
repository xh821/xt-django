from django.shortcuts import render ,HttpResponseRedirect,HttpResponse
from Dindan.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(redirect_field_name='',login_url='/login')
def zjdd1(request):
    if request.method =='POST':
        form = zjddForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['time']
            djbh = form.cleaned_data['djbh']
            dhsj = form.cleaned_data['dhsj']
            dhdw = form.cleaned_data['dhdw']
            spbh = form.cleaned_data['spbh']
            spmc = form.cleaned_data['spmc']
            sl = form.cleaned_data['sl']
            dj = form.cleaned_data['dj']
            je = form.cleaned_data['je']
            zdr = form.cleaned_data['zdr']
            sh = form.cleaned_data['sh']
            ZJDD = zjdd(
                time =time,djbh =djbh,dhsj =dhsj,dhdw =dhdw,
                spbh =spbh,spmc =spmc,sl =sl,dj =dj,
                je=je,zdr=zdr,sh =sh,
            )
            ZJDD.save()
            return HttpResponseRedirect('dd-shdd')
    else:
        form = zjddForm()
    return render(request,'dd-zjdd.html',{'form':form})


@login_required(redirect_field_name='',login_url='/login')
def shdd(request):
    SH = zjdd.objects.last()
    if request.method =='POST':
        form  = zjddForm(request.POST)
        if form.is_valid():
            sh = form.cleaned_data['sh']
            ZJDD =zjdd.objects.last().update(
                sh = sh
            )
            ZJDD.save()
            return  HttpResponseRedirect('dd-ddgl')
    else:
        form =zjddForm()
    return render(request,'dd-shdd.html',locals())

@login_required(redirect_field_name='',login_url='/login')
def ddgl(request):
    DDGL = zjdd.objects.all()
    return render(request,'dd-ddgl.html',locals())
