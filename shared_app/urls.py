from django.urls import path, include

import application_app.urls
import company_profiles_app.urls
import listing_app.urls

urlpatterns = [
    # Permissions

    path('', include(application_app.urls.permissions_urls)),
    path('', include(company_profiles_app.urls.permissions_urls)),
    path('', include(listing_app.urls.permissions_urls)),
]