from django.shortcuts import render
from  Chanpin.models import *
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(redirect_field_name='',login_url='/login')
def addsp1(request):
    if request.method =='POST':
        form =addspForm(request.POST)
        if form.is_valid():
            spmc = form.cleaned_data['spmc']
            spbh = form.cleaned_data['spbh']
            pp = form.cleaned_data['pp']
            gg = form.cleaned_data['gg']
            xh = form.cleaned_data['xh']
            zl = form.cleaned_data['zl']
            scsj = form.cleaned_data['scsj']
            bzq = form.cleaned_data['bzq']
            bxsj = form.cleaned_data['bxsj']
            ghxx = form.cleaned_data['ghxx']
            ckcb = form.cleaned_data['ckcb']
            ps = form.cleaned_data['ps']
            dwmc = form.cleaned_data['dwmc']
            dwdm =form.cleaned_data['dwdm']
            tm = form.cleaned_data['tm']
            lsj = form.cleaned_data['lsj']
            y1 = form.cleaned_data['y1']
            y2 = form.cleaned_data['y2']
            y3 = form.cleaned_data['y3']
            ADDSP = addsp(spmc =spmc,spbh=spbh,pp = pp,gg = gg,xh =xh,
            zl =zl,scsj =scsj,bzq=bzq,bxsj = bxsj,ghxx =ghxx,
            ckcb =ckcb,ps =ps,dwmc =dwmc,dwdm =dwdm,tm =tm,
            lsj =lsj,y1 = y1,y2 = y2,y3 = y3,)
            ADDSP.save()
            return  HttpResponseRedirect('cp-cpgl')
    else:
        form = addspForm()
    return render(request,'addsp.html',{'form':form})

@login_required(redirect_field_name='',login_url='/login')
def addspimg(request):
    if request.method =='POST':
        form = addspimgForm(request.POST,request.FILES)
        if form.is_valid():
             ADDSPIMG = addspimg.objects.create(
                 imgf =form.cleaned_data['imgf'],
                 imgb =form.cleaned_data['imgb'],
                 imgl =form.cleaned_data['imgl'],
                 imgr =form.cleaned_data['imgr'],
                 imgu =form.cleaned_data['imgu'],
                 imgd =form.cleaned_data['imgd'],
             )
             ADDSPIMG.save()
             return HttpResponseRedirect('addsp')
    else:
        form = addspimgForm()
    return render(request,'addspimg.html',{'form':form})


@login_required(redirect_field_name='',login_url='/login')
def cpgl(request):
     CPGL =  addsp.objects.all()
     return  render(request,'cp-cpgl.html',locals())