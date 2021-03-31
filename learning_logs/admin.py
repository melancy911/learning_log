from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic,Entry #文件名下的哪个py文件 从中引入某个类或函数
admin.site.register(Topic)
admin.site.register(Entry)