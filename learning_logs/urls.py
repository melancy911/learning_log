"""定义learning_logs的URL模式"""
#from django.conf.urls import url
#from . import views
#urlpatterns=[
    #主页
   # url(r'^$',views.index,name='index')
#]版本问题
from django.urls import path,re_path#re_path是正则表达式有效，path不能使正则表达式有效

#from . import views
#上述代码容易出现问报错Traceback (most recent call last):
  #File "/Users/congyan/PycharmProjects/learning_log/learning_logs/urls.py", line 10, in <module>
   # from . import views
#ImportError: attempted relative import with no known parent package
from . import views
app_name = 'learning_logs'

urlpatterns = [

    # 主页
    path(r'', views.index, name='index'),
    #显示所有主题
    re_path(r'^topics/$',views.topics,name='topics'),
    #特定主体的详细页面
    re_path(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
   #用于添加新主题的网页
    re_path(r'^new_topic$',views.new_topic,name='new_topic'),

    #用于添加新条目的页面
    #path(r'^new_entry/(?p<topic_id>\d+)/$',views.new_entry,name='nem_entry'),打错了
    re_path(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),#p都是大写   且正则表达式发挥作用要使用re_path
    #用于编辑条目的页面
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]

