from django.db import models

# Create your models here.
class CartInfo(models.Model):
    user=models.ForeignKey('user.UserInfo', on_delete=models.CASCADE)
    goods=models.ForeignKey('goods.GoodsInfo', on_delete=models.CASCADE)
    count=models.IntegerField()
