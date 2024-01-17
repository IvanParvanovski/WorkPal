from django.contrib import admin

from authentication_app.models.company import Company
from authentication_app.models.custom_user import CustomUser
from authentication_app.models.profile import Profile


admin.site.register(Profile)
admin.site.register(CustomUser)
admin.site.register(Company)
