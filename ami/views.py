from django.views.generic.base import TemplateView


class AmicoAppView(TemplateView):
    template_name = "app.html"
