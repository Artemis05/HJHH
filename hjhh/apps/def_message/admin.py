import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hjhh.settings")# project_name 项目名称
django.setup()
from django.contrib import admin
from .models import UserInfo

# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["uname", "usex", "uage", "upersonInf", "uemail", "ulogo", "ushou", "uaddress", "uyoubian", "uphone",
                    "urealname", "uzhengjian_type", "uzhengjian_tel", "uzhengjian_img", "ucheck_passOrfail",
                    "uname_passOrfail"]
    list_per_page = 5
    list_filter = ["uname", "uyoubian"]
    search_fields = ["uname", "uyoubian"]
    # 详情页面的只读字段
    readonly_fields = ["uname"]
    # 在列表页可以编辑的字段
    # list_editable = ["ucheck_passOrfail"]


admin.site.site_header = '后台管理系统'
admin.site.site_title = '后台管理系统'

admin.site.register(UserInfo, UserInfoAdmin)
