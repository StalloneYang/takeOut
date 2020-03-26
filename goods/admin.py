from django.contrib import admin
from .models import TypeInfo,GoodsInfo


# Register your models here.
class GoodsInfoline(admin.TabularInline):
 # class GoodsInfoline(admin.StackedInline):
    model = GoodsInfo
    extra = 2


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'isDelete']
    list_per_page = 10
    list_filter = ['title']
    search_fields = ['title']
    inlines = [GoodsInfoline]


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['gtitle', 'gpic', 'gprice', 'isDelete', 'gunit', 'gclick', 'gjianjie', 'gkucun', 'gcontent', 'gtype', 'gadv']
    list_per_page = 10
    list_filter = ['gtitle']
    search_fields = ['gtitle']


admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
