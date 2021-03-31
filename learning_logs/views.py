from django.shortcuts import render
from .models import Topic,Entry#记住这种导入方式 在自定义模块中导入某个类的方法
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse #django2.0 把原来的 django.core.urlresolvers 包 更改为了 django.urls
from .forms import TopicForm,EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')
@login_required
def topics(request):
    """显示所有主题"""
    topics=Topic.objects.filter(owner=request.user).order_by('date_added')
    context={'topics':topics}
    return render(request,'learning_logs/topics.html',context)#渲染成图像的
@login_required
def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    topic=Topic.objects.get(id=topic_id)
    #确认请求的主题属于当前用户
    if topic.owner !=request.user:
        raise Http404
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)
@login_required
def new_topic(request):#为什么要形参request（请求）
    """添加新主题"""
    if request.method!='POST':
        #未提交数据：创建一个新表单
        form=TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form=TopicForm(request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.owner=request.user
            new_topic.save()

            return  HttpResponseRedirect(reverse('learning_logs:topics'))
    context={'form':form}
    return render(request,'learning_logs/new_topic.html',context)
@login_required
def new_entry(request,topic_id):
    """在特定的主题中添加新条目"""
    topic=Topic.objects.get(id=topic_id)
    if request.method!='POST':
        #未提交数据，创建一个新的空表单
        form=EntryForm()
    else:
        #POST提交的数据，对数据进行处理
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    context={'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)#敲错了  应该是new_entry
@login_required
def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry=Entry.objects.get(id=entry_id)#此处报错是因为函数没有定义entry_id
    topic=entry.topic
    if topic.owner!=request.user:
        raise Http404
    if request.method!='POST':
        #初次请求，使用当前条目填充表单
        form=EntryForm(instance=entry)
    else:
        #POST提交的诗句，对数据进行处理
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context={'entry':entry,'topic':topic,'form':form}
    #return render(request,'learning_logs/edit.html',context)#报错  少打了个_entry
    return render(request, 'learning_logs/edit_entry.html', context)
#何时使用save(commit=False)方法

#Stackoverflow上其实已经有了一段非常精炼的答案。英文原文如下，我把它翻译了一下:

#That's useful when you get most of your model data from a form, but need to populate some null=False fields with non-form data. Saving with commit=False gets you a model object, then you can add your extra data and save it.

#当你通过表单获取你的模型数据，但是需要给模型里null=False字段添加一些非表单的数据，该方法会非常有用。如果你指定commit=False，那么save方法不会理解将表单数据存储到数据库，而是给你返回一个当前对象。这时你可以添加表单以外的额外数据，再一起存储。

#save(commit=False)方法实际应用案例

#下面我们来看一个实际应用案例。我们创建了一个叫文章Article的模型，里面包含title, body和作者author等多个字段，其中author字段非空null=False。我们由Article模型创建了一个ArticleForm表单，可以让用户发表新文章，但是我们故意把author字段除外了，因为我们不希望用户编辑作者。



#最后用户提交的表单数据里肯定没有author，当这样的数据提交到数据库时肯定会有问题的。所以我们先通过 article = form.save(commit=False)创建article实例，此时让Django先不要发送数据到数据库，等待我们把author添加好后，再把数据一起存储到数据库中。

