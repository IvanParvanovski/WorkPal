from django.views.generic import TemplateView


class ResponseSendAssociationRequest(TemplateView):
    template_name = 'responses/success_send_association_request.html'
