"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from django.urls import path   缺一个include


from django.urls import path, include,re_path

urlpatterns = [
    re_path('admin/', admin.site.urls),

    #path(r'^users/',include('users.urls',namespace='users')),报错，include（）中指定命名空间而不提供app_name是不被允许的，
    # 要在包含的模块中设置app_name属性或在包含的模块里面设置app_name变量。
    re_path(r'^users/',include(('users.urls','users'),namespace='users')),#记住这种用法
 #path(r'',include('learning_logs.urls',namespace='learning_logs'))
#上述代码报错：django.core.exceptions.ImproperlyConfigured: Specifying a namespace in
    # include() without providing an app_name is not supported.
    # Set the app_name attribute in the included module, or pass

    #a 2-tuple containing the list of patterns and app_name instead.

    #翻译过来是在include（）中指定命名空间而不提供app_name是不被允许的，要在包含的模块中设置app_name属性或在包含的模块里面设置app_name变量。

   path(r'', include(('learning_logs.urls', 'learning_logs'), namespace ='learning_logs')),



]
