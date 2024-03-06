from django.views.generic import TemplateView


class ControlPanelView(TemplateView):
    template_name = 'accounts_app/control_panel.html'

