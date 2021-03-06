from _sha1 import sha1

from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect

from goods.models import GoodsInfo
from order.models import OrderInfo
from user import user_decorator
from user.models import UserInfo
from django.shortcuts import render,redirect
# Create your views here.

def register(request):
    """注册页"""
    context = {'title':'注册'}
    return render(request,'user/register.html',context)

def register_handle(request):
    """注册判断"""
    user_table = request.POST
    user_name = user_table.get('user_name')
    pwd = user_table.get('pwd')
    cpwd = user_table.get('cpwd')
    email = user_table.get('email')
    allow = user_table.get('allow')

    # user_name、pwd还需加验证，注册失败，未勾选同意协议  给出对应的提示
    user_name_count = UserInfo.objects.filter(uname=user_name).count()
    email_count = UserInfo.objects.filter(uemail=email).count()
    if user_name_count>=1 or pwd!=cpwd or email_count>=1 or email=='' or user_name=='' or pwd=='' or cpwd=='' or allow=='':
        # context = {'title':'注册','error_name':0}
        return redirect('/user/register/')

    # 加密
    s1 = sha1()
    s1.update(pwd.encode("utf-8"))
    pwd_sha1 = s1.hexdigest()

    #写入数据库
    user = UserInfo()
    user.uname = user_name
    user.upwd = pwd_sha1
    user.uemail = email
    user.save()
    return redirect('/user/login/')

def login(request):
    """登录"""
    uname=request.COOKIES.get('uname','') # 如果上次登录有记住密码，这里就会把用户名填写进去
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'user/login.html',context)

def uname_exist(request):
    """判断用户名是否存在"""
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({"count": count})

def login_handle(request):
    """登录后判断用户名和密码是否正确"""
    uname = request.POST.get("username")
    password = request.POST.get("pwd")
    remember = request.POST.get("remember",0)
    user_name = UserInfo.objects.filter(uname=uname)  # 通过uname查数据库

    if uname == None:
        context = {'title':'用户登录', 'error_name': 0, 'error_pwd':0, 'uname':"", 'upwd':""}
        return render(request,'user/login.html',context)

    if user_name:
        s1 = sha1()
        s1.update(password.encode("utf-8"))  # 从接口拿到的密码加密
        if s1.hexdigest()==user_name[0].upwd:   # 对比数据库
            url=request.COOKIES.get('url','/goods/index/')
            red = HttpResponseRedirect(url)  # 重定向跳转到个人详情页，用这个才可以设置cookie信息
            # red = HttpResponseRedirect('/goods/index/')  # 重定向跳转到个人详情页，用这个才可以设置cookie信息
            if remember!=0:
                red.set_cookie("uname",uname)  # 把用户名传到cookie中
            else:
                red.set_cookie('uname','',max_age=-1)  # -1 立即失效
            request.session['user_id'] = user_name[0].id  # 在cookie中存入用户id，后面可以跟据id去查
            request.session['user_name'] = uname
            return red
        else:  # 用户名错误
            context = {'title':'用户登录', 'error_name': 0, 'error_pwd':1, 'uname':uname, 'upwd':password}
            return render(request,'user/login.html',context)
    else:  # 密码错误
        context = {'title':'用户登录', 'error_name': 1, 'error_pwd':0, 'uname':uname, 'upwd':password}
        return render(request,'user/login.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')

@user_decorator.login
def info(request):
    user_email=UserInfo.objects.get(id=request.session['user_id']).uemail

    # 最近浏览器
    goods_ids=request.COOKIES.get('goods_ids','')
    goods_ids1=goods_ids.split(',')
    goods_list=[]
    for goods_id in goods_ids1:
        if goods_id:
            goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))


    user_phone=UserInfo.objects.get(id=request.session['user_id']).uphone
    user_address=UserInfo.objects.get(id=request.session['user_id']).uaddress
    ureal_name=UserInfo.objects.get(id=request.session['user_id']).ureal_name
    user_name=request.session['user_name']
    context={'title':'用户中心', 'page_name':1, 'goods_list':goods_list, 'user_email': user_email, 'user_phone': user_phone, 'user_address': user_address, 'uname':user_name, 'ureal_name':ureal_name}
    return render(request,'user/user_center_info.html',context)

@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method=='POST':
        post=request.POST
        user.ureal_name=post.get('ureal_name')
        user.uaddress=post.get('uaddress')
        user.upostcode=post.get('uyoubian')
        user.uphone=post.get('uphone')
        user.save()
    context={'title':'用户中心', 'page_name':1, 'user':user}
    return render(request, 'user/user_center_site.html', context)

@user_decorator.login
def order(request,pindex):
    order_list = OrderInfo.objects.filter(user_id=request.session['user_id']).order_by('-oid')
    paginator = Paginator(order_list, 2)
    if pindex == '':
        pindex = '1'
    page = paginator.page(int(pindex))

    context = {'title': '用户中心',
               'page_name': 1,
               'paginator': paginator,
               'page': page, }
    return render(request, 'user/user_center_order.html', context)



