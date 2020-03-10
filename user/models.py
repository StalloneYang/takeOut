from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    uphone = models.CharField(max_length=11,default='')
    uaddress = models.CharField(max_length=100,default='')
    upostcode = models.CharField(max_length=10,default='')
    utelephone = models.CharField(max_length=11,default='')

    def __str__(self):
        return self.uname
