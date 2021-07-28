from django.views import generic as views


class HomePage(views.TemplateView):
    template_name = 'nails/index.html'
