from nails_project.common.forms import CommentForm
from tests.base.tests import NailsProjectTestCase


class TestCommentCreateForm(NailsProjectTestCase):

    def test_saveForm_whenValid_shouldBeValid(self):
        data = {
            'comment': "message",
        }
        form = CommentForm(data)
        self.assertTrue(form.is_valid())

    def test_saveForm_whenNotValid_shouldBeInValid_commentFieldError(self):
        data = {
            'comment': None,
        }
        form = CommentForm(data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(field='comment'))
