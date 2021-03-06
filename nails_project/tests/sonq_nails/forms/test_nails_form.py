from os.path import join
import random
from django.test import override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile
from nails_project import settings
from nails_project.sonq_nails.forms import NailsForm
from nails_project.sonq_nails.models import Nails
from tests.base.tests import NailsProjectTestCase


class TestNailsCreateForm(NailsProjectTestCase):
    path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test.jpg')
    file_name = f'{random.randint(1, 10000)}-test.jpg'
    file_data = {'image': SimpleUploadedFile(
        name=file_name,
        content=open(path_to_image, 'rb').read(),
        content_type='image/jpeg',
    )}

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_saveForm_whenValid_shouldBeValid(self):
        data = {
            'type': Nails.MANICURE,
            'feedback': Nails.POSITIVE,
            'description': "description",
        }
        form = NailsForm(data, self.file_data)
        self.assertTrue(form.is_valid())

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_saveForm_whenNotValid_shouldBeInValid_typeFieldError(self):
        data = {
            'type': None,
            'feedback': Nails.POSITIVE,
            'description': "description",
        }
        form = NailsForm(data, self.file_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(field='type'))

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_saveForm_whenNotValid_shouldBeInValid_feedbackFieldError(self):
        data = {
            'type': Nails.MANICURE,
            'feedback': None,
            'description': "description",
        }
        form = NailsForm(data, self.file_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(field='feedback'))

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_saveForm_whenNotValid_shouldBeInValid_ImageFieldError(self):
        data = {
            'type': Nails.MANICURE,
            'feedback': Nails.POSITIVE,
            'description': "description",
        }
        form = NailsForm(data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(field='image'))
