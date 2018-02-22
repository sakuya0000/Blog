from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .usersForm import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@csrf_exempt
def regist(request):
    if request.method == 'POST':
        userform = Users(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['name']
            user = User.objects.filter(username__exact=username)
            if user:
                return HttpResponse('用户名已注册')
            else:
                password = userform.cleaned_data['password']
                email = userform.cleaned_data['email']
                User.objects.create(username=username, password=password, email=email)#存储数据
                request.session['username'] = username
                request.session['visitname'] = username
                return HttpResponseRedirect('/index')
    else:
        userform = Users()
    return render_to_response('Register.html', {'userform': userform})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        userform = Users(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['name']
            password = userform.cleaned_data['password']
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                request.session['username'] = username
                request.session['visitname'] = username
                return HttpResponseRedirect('/index')
            else:
                return HttpResponse('用户名或密码错误')
    else:
        userform = Users()
    return render_to_response('Login.html', {'userform': userform})


def get_blogs(request):
    username = request.session.get('username')
    if username:
        blogs_list = Blog.objects.all().order_by('-pub')#获得所有的博客按时间排序
        paginator = Paginator(blogs_list, 5)
        page = request.GET.get('page')
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        return render_to_response('index.html', {'blogs': blogs})#传递context:blog参数到固定页面。
    else:
        return HttpResponseRedirect('/login')


def get_details(request, blog_id):
    username = request.session.get('username')
    if username:
        try:
            blog = Blog.objects.get(id=blog_id)#获取固定的blog_id的对象；
        except Blog.DoesNotExist:
            raise Http404

        if request.method == 'GET':
            form = CommentForm()
        else:  #请求方法为Post
            form = CommentForm(request.POST)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                cleaned_data['blog'] = blog
                cleaned_data['name'] = username
                Comment.objects.create(**cleaned_data)
        ctx = {
            'blog': blog,
            'comments': blog.comment_set.all().order_by('-pub'),
            'form': form
        }#返回3个参数
        return render(request, 'blog_details.html', ctx)#######
    else:
        return HttpResponseRedirect('/login')
