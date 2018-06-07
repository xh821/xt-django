from django.shortcuts import render,HttpResponseRedirect
from Kehu.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(redirect_field_name='',login_url='/login')
def khxx1(request):
    if request.method =='POST':
        form = khxxForm(request.POST)
        if form.is_valid():
            khbh = form.cleaned_data['khbh']
            khmc = form.cleaned_data['khmc']
            khlx = form.cleaned_data['khlx']
            khdj = form.cleaned_data['khdj']
            khyh = form.cleaned_data['khyh']
            yhzh = form.cleaned_data['yhzh']
            xsry = form.cleaned_data['xsry']
            lxr = form.cleaned_data['lxr']
            tel = form.cleaned_data['tel']
            tel2 = form.cleaned_data['tel2']
            dz = form.cleaned_data['dz']
            sfzh = form.cleaned_data['sfzh']
            KHXX = khxx(
                khbh = khbh,khmc = khmc,khlx =khlx,khdj =khdj,
                khyh =khyh,yhzh = yhzh,xsry =xsry,lxr =lxr,tel =tel,
                tel2 =tel2,dz =dz,sfzh =sfzh,
            )
            KHXX.save()
            return HttpResponseRedirect('/Kehu/khgl')
    else:
        form = khxxForm()
    return render(request,'kh-khxx.html',{'form':form})

@login_required(redirect_field_name='',login_url='/login')
def khgl(request):
    KHXX = khxx.objects.all()
    return  render(request,'kh-khgl.html',locals())

