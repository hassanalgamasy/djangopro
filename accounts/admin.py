from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Register your models here.
class UserAdmin(BaseUserAdmin):

    list_display=('username', 'email', 'phone', 'account_type')
    search_fields=('phone', 'email', 'phone')
    fieldsets= BaseUserAdmin.fieldsets + (
        (None, {'fields':('account_type', 'balance')}),
    )
    add_fieldsets= BaseUserAdmin.add_fieldsets + (
    (None, {'fields':('phone', 'account_type', 'balance')}),
    )

admin.site.register(User,UserAdmin)