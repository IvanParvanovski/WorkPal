from django.urls import path

from accounts_app.views.authentication_views import SignUpView, SignInView, sign_out_view
from accounts_app.views.control_panel_views import ControlPanelView

urlpatterns = [
    path('sign_in/', SignInView.as_view(), name='sign_in'),
    path('sign_up/', SignUpView.as_view(), name='sign_up'),
    path('sign_out', sign_out_view, name='sign_out'),
    path('control_panel', ControlPanelView.as_view(), name='control_panel')
]
