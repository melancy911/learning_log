"""为应用程序定义URL模式"""
#from django.conf.urls import url版本问题 ，

#from django.urls import path
#from django.contrib.auth.views import login#报错   没有这个函数了 版本问题
#from django.conf.urls import url
#from django.contrib.auth.views import LoginView  #login函数已经变成了LoginView类
#from . import views

#urlpatterns=[
    #登录页面
    #url(r'^login/$',login,{'template_name':'users/login.html'},name='login')
#]
from django.urls import path,re_path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'users'

urlpatterns = [
    # 登录页面
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    #注销
    re_path(r'^logout/$',views.logout_view,name='logout'),
    #注册页面
    re_path(r'^register/$',views.register,name='register'),

]
