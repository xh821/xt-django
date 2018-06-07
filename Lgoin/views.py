from django.shortcuts import render,HttpResponseRedirect,HttpResponse,render_to_response
from django.contrib import  auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
 #权限设置

from django import  forms

class userForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)
    last_name = forms.CharField()

class USERForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)


def register_view(request):
    context = {}
    if request.method =='POST':
        form = userForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            last_name = form.cleaned_data['last_name']
            user = auth.authenticate(username = username,password = password,last_name =last_name)
            if user:
                context['userExit'] = True
                return render(request,'register.html',context)

            user = User.objects.create_user(username = username,password = password,last_name =last_name)
            user.save()
            request.session['username'] = username
            # auth.login(request,username)
            LAST_NAME = int(last_name)
            if LAST_NAME == 0:
                auth.login(request, user)
                request.session['username'] = username
                return render_to_response('dd-ddgl.html',{'username':username})

            elif LAST_NAME == 1:
                auth.login(request, user)
                request.session['username'] = username
                return render_to_response('cw-rkd.html',{'username':username})

            elif LAST_NAME == 2:
                auth.login(request, user)
                request.session['username'] = username
                return render_to_response('yg-yggl.html',{'username':username})

            elif LAST_NAME == 3:
                auth.login(request, user)
                request.session['username'] = username
                return render_to_response('ck-rkd.html',{'username':username})

            elif LAST_NAME == 4:
                auth.login(request, user)
                request.session['username'] = username
                return render_to_response('index.html',{'username':username})
    else:
        context = {'isLogin':False}

    return  render(request,'register.html',context)



def login_view(request):
    context = {}
    if request.method == 'POST':
        form = USERForm(request.POST)
        if form.is_valid():
            #获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = authenticate(username = username,password = password)
            if user:
                #比较成功，跳转index
                auth.login(request, user)
                request.session['username'] = username
                Result = User.objects.filter(username = username).values()
                bum = Result[0]['last_name']
                last_name =int(bum)
                if last_name == 0:
                    auth.login(request, user)
                    request.session['username'] = username
                    return  render_to_response('dd-ddgl.html',{'username':username})

                elif last_name == 1:
                    auth.login(request, user)
                    request.session['username'] = username
                    return  render_to_response('cw-rkd.html',{'username':username})

                elif last_name == 2:
                    auth.login(request, user)
                    request.session['username'] = username
                    return  render_to_response('yg-yggl.html',{'username':username})

                elif last_name == 3:
                    auth.login(request, user)
                    request.session['username'] = username
                    return  render_to_response('ck-rkd.html',{'username':username})

                elif last_name == 4:
                    auth.login(request, user)
                    request.session['username'] = username
                return  render_to_response('index.html',{'username':username})
            else:
                ##比较失败，还在login
                context = {'isLogin': False,'pawd':False}
                return render(request,'login.html', context)
    else:
        context = {'isLogin': False,'pswd':True}
        return  render(request, 'login.html', context)




# def CESHI(request):
#     return render(request,'CESHI.html',{'last_name':last_name})

class WeiXinLogin():
    appid = 'wxe0d95453c412f118'
    appsecret = 'd785bt925fbc7ebed62734cfdpe5951c'
    code = ''
    state = ''


# def get_info(self):
#
#         # 第一步获取code跟state
#     try:
#         self.code = self.request.GET.get("code")
#         self.state = self.request.GET.get("state")
#     except Exception, e:
#         add_log.info("获取code和stat参数错误：\n%s" % str(traceback.format_exc()))
#
#         # 2.通过code换取网页授权access_token
#     try:
#         url = u'https://api.weixin.qq.com/sns/oauth2/access_token'
#         params = {
#             'appid': self.appid,
#             'secret': self.appsecret,
#             'code': self.code,
#             'grant_type': 'authorization_code'
#         }
#         res = requests.get(url, params=params).json()
#     except Exception, e:
#         add_log.info("获取access_token参数错误：\n%s" % str(traceback.format_exc()))
#         raise Http404()
#
#
#     try:
#         user_info_url = u'https://api.weixin.qq.com/sns/userinfo'
#         params = {
#             'access_token': res["access_token"],
#             'openid': res["openid"],
#         }
#         res = requests.get(user_info_url, params=params).json()
#     except Exception, e:
#         add_log.info("拉取用户信息错误：\n%s" % str(traceback.format_exc()))

# def Pic():
#     _data = []
#     for t in range(0, 25000):
#         _t = t / 1000
#         x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
#         y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
#         z = _t + 2.0 * math.sin(75 * _t)
#         _data.append([x, y, z])
#     range_color = [
#         '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
#         '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
#     line3d = Line3D("3D line plot demo", width=1200, height=600)
#     line3d.add("", _data, is_visualmap=True,
#                visual_range_color=range_color, visual_range=[0, 30],
#                is_grid3D_rotate=True, grid3D_rotate_speed=180)
#     return line3d




