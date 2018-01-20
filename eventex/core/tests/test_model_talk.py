from django.test import TestCase
from eventex.core.models import Talk


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title = 'Título da palestra'
        )
    
    def test_create(self):
        self.assertTrue(Talk.objects.exists())
    
    def test_has_speaker(self):
        """ Talk has many speakers and vice-versa """
        self.talk.speakers.create(
            name='Marcelo Andriolli',
            slug='henrique-bastos',
            website='http://marceloandriolli.net'
        )
        self.assertEqual(1, self.talk.speakers.count())
    
    def test_description_black(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speakers_black(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)
    
    def test_start_black(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)
    
    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da palestra', str(self.talk))
