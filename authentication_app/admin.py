from django.contrib import admin

from authentication_app.models.custom_user import CustomUser

# Register your models here.
admin.site.register(CustomUser)
