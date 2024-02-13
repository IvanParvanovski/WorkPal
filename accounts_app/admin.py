from django.contrib import admin

from accounts_app.models.custom_user import CustomUser
from accounts_app.models.profile import Profile


admin.site.register(Profile)
admin.site.register(CustomUser)
