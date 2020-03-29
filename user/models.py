from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=100)  # 用户名
    ureal_name=models.CharField(max_length=100,default='')  # 真实姓名
    upwd = models.CharField(max_length=100)  # 密码
    uemail = models.CharField(max_length=100)  # 邮箱
    uphone = models.CharField(max_length=100,default='无')  # 手机--
    uaddress = models.CharField(max_length=100,default='无')  # 地址
    upostcode = models.CharField(max_length=100,default='无')  # 邮编 ---
    utelephone = models.CharField(max_length=100,default='无')  # 电话---

    def __str__(self):
        return self.uname
