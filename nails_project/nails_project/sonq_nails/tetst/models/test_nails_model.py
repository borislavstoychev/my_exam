from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from nails_project.accounts.models import NailsUser
from nails_project.sonq_nails.models import Nails


class TestNails(TestCase):
    user = NailsUser.objects.create_user(
        email="just-for-testing@testing.com",
        password1="dummy-insecure",
    )
    data = {
        'type': 'Manicure',
        'feedback': 'Positive',
        'description': 'beautiful',
        'image': SimpleUploadedFile(name='test_image.jpg', content=open('media/images/nails/test.jpg', 'rb').read(),
                                    content_type='image/jpeg'),
        'user': user
    }

    def test_saveModel_whenValid_shouldBeValid(self):
        obj = Nails(**self.data)
        obj.full_clean()
        obj.save()
