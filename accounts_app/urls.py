from django.urls import path

from accounts_app.views import SignUpCreateView

# from accounts_app.views import SignInView, SignUpView

urlpatterns = [
    # path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('sign_up/', SignUpCreateView.as_view(), name='sign_up'),
]
