import os

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from nails_project import settings
from nails_project.sonq_nails.forms import NailsForm


class TestNailsCreateForm(TestCase):
    path_to_image = os.path.join(settings.BASE_DIR, "media/images/nails/test.jpg")
    data = {
        'type': 'Manicure',
        'feedback': 'Positive',
        'description': 'beautiful',
        'image': File(open(path_to_image, 'rb'))
    }

    def test_saveForm_whenValid_shouldBeValid(self):
        type = 'Manicure'
        feedback = 'Positive'
        description = 'beautiful'
        image = File(open(self.path_to_image, 'rb'))
        user = 'borko@mail.bg'
        form = NailsForm(data={
            'type': type,
            'feedback': feedback,
            'description': description,
            'image': image,
        })
        print(form.errors)
        self.assertTrue(form.is_valid())


