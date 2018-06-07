from django.shortcuts import render,HttpResponseRedirect
from Yuang.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(redirect_field_name='',login_url='/login')
def ygxxadd(request):
    if request.method =='POST':
        form = ygxxForm(request.POST)
        if form.is_valid():
            bh = form.cleaned_data['bh']
            name =form.cleaned_data['name']
            tel = form.cleaned_data['tel']
            bum = form.cleaned_data['bum']
            sfzh = form.cleaned_data['sfzh']
            gzkh = form.cleaned_data['gzkh']
            rzsj = form.cleaned_data['rzsj']
            YGXX = ygxx(
                bh =bh,name =name,tel =tel,
                bum =bum,sfzh = sfzh,gzkh =gzkh,
                rzsj =rzsj,
            )
            YGXX.save()
            return HttpResponseRedirect('/Yuang/ygxxgl')
    else:
        form =ygxxForm()
    return render(request,'yg-ygxx.html',{'form':form})

@login_required(redirect_field_name='',login_url='/login')
def ygxxgl(request):
    YGXXGL = ygxx.objects.all()
    return render(request,'yg-yggl.html',locals())


