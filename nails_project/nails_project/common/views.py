from django.views import generic as views

from nails_project.sonq_nails.views import NailsListView


class HomePage(NailsListView):
    template_name = 'nails/index.html'

