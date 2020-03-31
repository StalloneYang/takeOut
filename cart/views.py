from django.shortcuts import render,redirect
from user import user_decorator
from .models import CartInfo
from django.http import JsonResponse


@user_decorator.login
def cart(request):
    uid=request.session['user_id']
    carts=CartInfo.objects.filter(user_id=uid)
    context={'title':'购物车','page_name':1,'carts':carts}
    return render(request,'cart/cart.html',context)

@user_decorator.login
def add(request,gid,count):
    # 用户uid购买了gid商品，数量为count
    uid=request.session['user_id']
    gid=int(gid)
    count=int(count)
    # 检查购物车中是否有该商品,有则增加数量，无则新增
    carts=CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts)>=1:
        cart=carts[0]
        cart.count=cart.count+count
    else:
        cart=CartInfo()
        cart.user_id=uid
        cart.goods_id=gid
        cart.count=count
    cart.save()

    if request.is_ajax():
        count=CartInfo.objects.filter(user_id=request.session['user_id'].count())
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')



def edit(request,gid):
    pass

def delete(request,gid):
    pass