from django.contrib import admin

from .models import User

# =======================================================
# Controls the fields to display in admin panel
# =======================================================


class UserAdmin(admin.ModelAdmin):
    list_display = ('id',                     
                  'user_id', 
                  'user_name',
                  'user_mobile',
                  'user_email',
                  'user_password'
                    )
admin.site.register(User, UserAdmin)