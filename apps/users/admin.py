from django.contrib import admin
from users.models import VerifyCode

# Register your models here.


class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'mobile', "add_time"]
    search_fields = ['mobile', 'code']


admin.site.register(VerifyCode, VerifyCodeAdmin)