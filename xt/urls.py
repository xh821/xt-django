"""xt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from  django.conf.urls.static import static
from Lgoin import views as viewsl
from index import views as viewsi


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('Cangk/',include('Cangk.urls',namespace='Cangk')),
    path('Caiwu/',include('Caiwu.urls',namespace='Caiwu')),
    path('Chanpin/',include('Chanpin.urls',namespace='Chanpin')),
    path('Dindan/',include('Dindan.urls',namespace='Dindian')),
    path('Kehu/',include('Kehu.urls',namespace='Kehu')),
    path('Yuang/',include('Yuang.urls',namespace='Yuang')),
    path('Lgoin/',include('Lgoin.urls',namespace='Lgoin')),

    path('index', viewsi.index,name='index'),
    path('register',viewsl.register_view,name= 'register'),
    path('login',viewsl.login_view,name ='login'),
    path('Liuyan',viewsi.Liuyan,name = 'Liuyan')




]

# urlpatterns += static('/', document_root=settings.STATIC_ROOT)