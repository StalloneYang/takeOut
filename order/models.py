from django.db import models

# Create your models here.
class OrderInfo(models.Model):
    oid=models.CharField(max_length=20, primary_key=True)
    user=models.ForeignKey('user.UserInfo', on_delete=models.CASCADE)
    odate=models.DateTimeField(auto_now_add=True)
    oIsPay=models.BooleanField(default=False)
    ototal=models.DecimalField(max_digits=6,decimal_places=2)
    oaddress=models.CharField(max_length=150)

#无法实现：真实支付，物流信息

class OrderDetailInfo(models.Model):
    goods=models.ForeignKey('goods.GoodsInfo', on_delete=models.CASCADE)
    order=models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    count=models.IntegerField()
