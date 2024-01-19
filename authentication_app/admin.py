from django.contrib import admin

from authentication_app.models.custom_user import CustomUser
from authentication_app.models.profile import Profile


admin.site.register(Profile)
admin.site.register(CustomUser)
