from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class TypeInfo(models.Model):
    title=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    # def __str__(self):
    #     return self.title.encode('utf-8')


class GoodsInfo(models.Model):
    gtitle=models.CharField(max_length=20)  # 名称
    gpic=models.ImageField(upload_to='goods')  # 图片地址
    gprice=models.DecimalField(max_digits=5,decimal_places=2)  # 价格
    isDelete=models.BooleanField(default=False)  # 是否删除
    gunit=models.CharField(max_length=20, default='500')  # 单位
    gclick=models.IntegerField()  # 点击量
    gjianjie=models.CharField(max_length=200)  # 简介
    gkucun=models.IntegerField()  # 库存
    gcontent=HTMLField()  # 详情介绍
    gtype=models.ForeignKey("TypeInfo", on_delete=models.CASCADE)  # 类型 5-10
    gadv=models.IntegerField(default=False)  # 广告、推荐（暂时用不到）
    # def __str__(self):
    #     return self.gtitle.encode('utf-8')


