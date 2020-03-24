from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)  # 用户名
    upwd = models.CharField(max_length=40)  # 密码
    uemail = models.CharField(max_length=30)  # 邮箱
    uphone = models.CharField(max_length=11,default='')  # 手机--
    uaddress = models.CharField(max_length=100,default='')  # 地址
    upostcode = models.CharField(max_length=10,default='')  # 邮编 ---
    utelephone = models.CharField(max_length=11,default='')  # 电话---

    def __str__(self):
        return self.uname
