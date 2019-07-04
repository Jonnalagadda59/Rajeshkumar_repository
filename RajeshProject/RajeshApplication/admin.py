from django.contrib import admin
from .models import UserData
class AdminUserData(admin.ModelAdmin):
    list_display = ['firstname',
                    'lastname',
                    'mobile',
                    'states',
                    'subject',]
admin.site.register(UserData,AdminUserData)