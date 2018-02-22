from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .users import *
from .models import User
from django.views.decorators.csrf import csrf_exempt


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
                response = HttpResponseRedirect('/login')
                userid = User.objects.get(username=username, password=password, email=email)
                response.set_cookie('userid', userid, 'visitid', userid)#存cookie
                return response
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
                return render_to_response('')
            else:
                return HttpResponse('用户名或密码错误')
    else:
        userform = Users()
    return render_to_response('Login.html', {'userform': userform})
