from django.contrib import admin
from .models import UserInfo



class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id','uname', 'upwd', 'uemail', 'uphone', 'uaddress', 'upostcode','utelephone']
    list_per_page = 10
    list_filter = ['uname']
    search_fields = ['uname']



admin.site.register(UserInfo,UserInfoAdmin)