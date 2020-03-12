from django.contrib import admin
from app1.models import GetDB, PostDB

class GetDBAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'address', 'data']


class PostDBAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'address', 'message', 'file_name', 'data']


class LoginAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip', 'address', 'data']


# Register your models here.
admin.site.register(GetDB, GetDBAdmin)
admin.site.register(PostDB, PostDBAdmin)
# admin.site.register(LoginUser, LoginAdmin)
