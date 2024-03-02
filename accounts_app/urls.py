from django.urls import path

from accounts_app.views import SignUpView, SignInView, sign_out_view

urlpatterns = [
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_out', sign_out_view, name='sign_out')
]
