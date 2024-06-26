"""
URL configuration for WorkPal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

import application_app.urls
import company_profiles_app.urls
import listing_app.urls
from WorkPal import settings
from WorkPal.views import HomeView, custom_page_404_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),

    # Included namespaces
    path('accounts/', include('accounts_app.urls')),
    path('dashboard/', include('dashboard_app.urls')),
    path('permissions/', include('shared_app.urls')),

    # Included pattern lists of urls
    path('', include(listing_app.urls.main_urls)),
    path('applications/', include(application_app.urls.main_urls)),
    path('companies/', include(company_profiles_app.urls.main_urls)),
]

handler404 = 'WorkPal.views.custom_page_404_not_found'
handler403 = 'WorkPal.views.custom_page_403_forbidden'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
