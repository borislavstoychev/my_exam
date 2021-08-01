from nails_project.sonq_nails.models import Nails


class NailsService:
    def __init__(self, state):
        self.state = state

    def get_by_state(self):
        if self.state == 'M':
            return Nails.objects.filter(type="Manicure")
        elif self.state == 'P':
            return Nails.objects.filter(type="Pedicure")
        else:
            return Nails.objects.all()

