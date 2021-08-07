import os
from os.path import join
import random
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from nails_project import settings
from nails_project.sonq_nails.forms import NailsForm
from nails_project.sonq_nails.models import Nails
from tests.base.tests import NailsProjectTestCase


class TestNailsCreateForm(NailsProjectTestCase):
    path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test.jpg')
    file_name = f'{random.randint(1, 10000)}-test.jpg'
    file = SimpleUploadedFile(
        name=file_name,
        content=open(path_to_image, 'rb').read(),
        content_type='image/jpeg')
    #

    def test_saveForm_whenValid_shouldBeValid(self):
        self.client.force_login(self.user)
        type = Nails.MANICURE
        feedback = Nails.POSITIVE
        description = 'beautiful'
        user = 'borko@mail.bg'
        form = NailsForm(data={
            'type': type,
            'feedback': feedback,
            'description': description,
            'image': self.path_to_image,
            'user': self.user,
        })
        print(form.errors)
        self.assertTrue(form.is_valid())