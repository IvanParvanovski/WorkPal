from django.urls import path

from listing_app.views import test_slider

urlpatterns = [
    path('', test_slider),
]
