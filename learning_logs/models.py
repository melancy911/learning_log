from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)#属性date——added是用来对topic对象进行排序的和text使用来限制长度的
    #owner=models.ForeignKey(User)报错，版本问题(to=User,on_delete=models.CASCADE)，
    # 听说(to=User,on_delete=models.DO_NOTHING)也行 但没试过
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='entries'
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50]+"..."