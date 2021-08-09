from unittest.mock import patch
from os.path import join
import random
import tempfile
from nails_project import settings
from django.test import override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from nails_project.sonq_nails.forms import NailsForm
from nails_project.sonq_nails.models import Nails
from tests.base.tests import NailsProjectTestCase


class SignalsNails(NailsProjectTestCase):
    path_to_image = join(settings.BASE_DIR, 'tests', 'media', 'test.jpg')
    file_name = f'{random.randint(1, 10000)}-test.jpg'
    file_data = {'image': SimpleUploadedFile(
        name=file_name,
        content=open(path_to_image, 'rb').read(),
        content_type='image/jpeg',
    )}

    @patch('nails_project.sonq_nails.signals')
    def test_question_posted_signal_triggered(self, mock):
        data = {
            'type': Nails.MANICURE,
            'feedback': Nails.POSITIVE,
            'description': "description",
        }
        form = NailsForm()
        form.save()

        # Check that your signal was called.
        self.assertTrue(mock.called)

        # Check that your signal was called only once.
        self.assertEqual(mock.call_count, 1)