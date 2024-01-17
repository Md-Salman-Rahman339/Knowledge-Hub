from django.contrib import admin

# Register your models here.
from .models import UserAccount, UserAddress


admin.site.register(UserAccount)
admin.site.register(UserAddress)