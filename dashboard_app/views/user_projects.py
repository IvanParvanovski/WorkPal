from django.views.generic import TemplateView


class UserProjectsView(TemplateView):
    template_name = 'dashboard/user_projects.html'
