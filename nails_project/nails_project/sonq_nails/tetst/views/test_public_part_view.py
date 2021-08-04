from django.test import TestCase, Client
from django.urls import reverse


class TestIndex(TestCase):

    def setUp(self):
        self.test_client = Client()

    def test_getIndex_whenNoObjects_shouldRenderCorrectTemplateWithNoObjects(self):
        response = self.test_client.get(reverse('home'))
        self.assertTemplateUsed(response, 'nails/index.html')
        obj = response.context['nails']
        self.assertEqual(0, len(obj))


class TestNailsListView(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getIndex_whenNoObjects_shouldRenderCorrectTemplateWithNoObjects(self):
        response = self.test_client.get(reverse('list nails'))
        self.assertTemplateUsed(response, 'nails/nails_list.html')
        obj = response.context['nails']
        self.assertEqual(0, len(obj))