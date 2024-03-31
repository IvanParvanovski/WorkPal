from django.views.generic import TemplateView


class ResponseCreateNewCompany(TemplateView):
    template_name = 'responses/success_create_company.html'
