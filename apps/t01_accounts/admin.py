from django.contrib import admin

# Register your models here.

from .models import CustomUser
from tabbed_admin import TabbedModelAdmin
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # list_display = ('id','username','email','is_active','is_superuser','last_login','is_staff','date_joined','last_login')
    list_display = (
        'id', 'username', 'email', 'is_active', 'is_superuser', 'last_login', 'is_staff', 'last_login')

    list_display_links = ('id', 'username', 'email', 'is_active')

    # 画面レイアウトの項目配置
    fieldsets = (
        ('⏬ 基本情報：', {
            'classes': ('grp-collapse grp-open',),
            'fields':
                (
                    # 'username','first_name','last_name','email', 'password',
                    'username', 'email', 'password',
                ),
            'description': '⏬⏬ ユーザー基本情報を記載',
        })
        ,
        ('⏬ 権限設定：', {
            'classes': ('grp-collapse grp-open',),
            'fields':
                (
                    'groups', 'user_permissions',
                    ('is_active', 'is_staff', 'is_superuser'),
                ),
            'description': '⏬⏬ ユーザーのアクセス権限を設定',
            # 'classes': ('collapse', 'closed'),  # エリアの表示・非表示設定
        })
    )
    save_as = True
    tabs = [
        ('ユーザー情報', fieldsets),
    ]
