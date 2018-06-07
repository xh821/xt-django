from django.shortcuts import render
from Caiwu.models import *
from django.shortcuts import HttpResponseRedirect ,HttpResponse
from django.contrib.auth.decorators import login_required
from PIL import Image
import qrcode
import datetime
import time
# from io import StringIO
# from xhtml2pdf import pisa
# from django.template.loader import get_template
# from django.template import  Context
# from cgi import escape


# #PDF
# def render_to_pdf(template_src, context_dict):
#     template = get_template(template_src)
#     context = Context(context_dict)
#     html  = template.render(context)
#     result = StringIO.StringIO()
#     pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))


@login_required(redirect_field_name='',login_url='/login')
def addrkd(request):
    if request.method == "POST":
        form = cwrkdForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['time']
            djbh = form.cleaned_data['djbh']
            fkdw = form.cleaned_data['fkdw']
            jsr = form.cleaned_data['jsr']
            bm = form.cleaned_data['bm']
            fjsm = form.cleaned_data['fjsm']
            ps1 = form.cleaned_data['ps1']
            ysje = form.cleaned_data['ysje']
            yfje = form.cleaned_data['yfje']
            zhbh = form.cleaned_data['zhbh']
            zhmc = form.cleaned_data['zhmc']
            jsfs = form.cleaned_data['jsfs']
            je = form.cleaned_data['je']
            ps = form.cleaned_data['ps']
            zdr = form.cleaned_data['zdr']
            CWRKD = cwrkd(time = time,djbh =djbh,fkdw = fkdw,
                          jsr =jsr,bm =bm,fjsm =fjsm,ps1 =ps1,
                          ysje = ysje,yfje =yfje,zhbh =zhbh,zhmc = zhmc,
                          jsfs= jsfs,je= je,ps=ps,zdr=zdr,)
            CWRKD.save()
            return HttpResponseRedirect('/Caiwu/cw-jslr')
    else:
        form = cwrkdForm()
    return render(request, 'cw-rkd.html', {'form':form})
@login_required(redirect_field_name='',login_url='/login')
def addckd(request):
    if request.method == "POST":
        form = cwckdForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['time']
            djbh = form.cleaned_data['djbh']
            fkdw = form.cleaned_data['fkdw']
            jsr = form.cleaned_data['jsr']
            bm = form.cleaned_data['bm']
            fjsm = form.cleaned_data['fjsm']
            ps1 = form.cleaned_data['ps1']
            ysje = form.cleaned_data['ysje']
            yfje = form.cleaned_data['yfje']
            zhbh = form.cleaned_data['zhbh']
            zhmc = form.cleaned_data['zhmc']
            jsfs = form.cleaned_data['jsfs']
            je = form.cleaned_data['je']
            ps = form.cleaned_data['ps']
            zdr =form.cleaned_data['zdr']
            CWRKD = cwckd(time=time, djbh=djbh, fkdw=fkdw,
                          jsr=jsr, bm=bm, fjsm=fjsm, ps1=ps1,
                          ysje=ysje, yfje=yfje, zhbh=zhbh, zhmc=zhmc,
                          jsfs=jsfs, je=je, ps=ps,zdr=zdr,)
            CWRKD.save()
            return HttpResponseRedirect('/Caiwu/cw-jslr')
    else:
        form = cwckdForm()
    return render(request, 'cw-ckd.html', {'form': form})

@login_required(redirect_field_name='',login_url='/login')
def jslr(request):
    if request.method == "POST":
        form = jslrForm(request.POST)
        if form.is_valid():
            start_time = form.cleaned_data['qssj']
            end_time = form.cleaned_data['jssj']
            CKD = cwckd.objects.all().filter(time__range=(start_time,end_time))
            RKD = cwrkd.objects.all().filter(time__range=(start_time,end_time))
            sum = 0
            SUM = 0
            for id in RKD:
                RJE = id.je
                sum = sum + RJE
            for id in CKD:
                CJE = id.je
                SUM =SUM + CJE
            lr = sum - SUM
            LR = str(lr)
            qr = qrcode.QRCode(
                version=2,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size = 50,
                border=1
            )
            content="时间：利润：",start_time,end_time,LR
            qr.add_data(content)
            qr.make(fit=True)
            img = qr.make_image()
            img.save("./tmp/lr.png")
            # return render_to_pdf(
            #     'cw-jslr.html',
            #     {
            #         'pagesize': 'A4',
            #         'mylist': form,
            #     }
            # )
            # response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment;filename=利润清单.pdf'
            # buffer = StringIO()
            # p = canvas.Canvas(buffer)
            # LR = str(lr)
            # p.drawText()
            # # p.drawString(400, 400, LR)
            # p.showPage()
            # p.save()
            # pdf = buffer.getvalue()
            # buffer.close()
            # response.write(pdf)
    return render(request,'cw-jslr.html',locals())









